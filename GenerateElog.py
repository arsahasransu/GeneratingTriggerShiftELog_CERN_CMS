from prettytable import PrettyTable

import re
import requests

def TTAdd(time, text, indent=0):
    return "    "*indent + "[" + time + "] " +  text + "\n"

def TAdd(text, indent=0):
    return "    "*(indent+1) + "- " + text + "\n"

def BR(time, run, summary):
    text = "\n====================================\n"
    text += TTAdd(str(time), "Run " + str(run) + " started: " + summary + ".\n\n")
    return text

def ER(time, run):
    text = '\n'
    text += TTAdd(str(time), "Run " + str(run) + " stopped.")
    text += "====================================\n"
    return text

def RunSAdd(tkey, ps, lhcstat, ss, tss):
    text = "    - Configuration: \n"
    text += "        - LHC status: " + str(lhcstat) + "\n"
    text += "        - Trigger Key: " + str(tkey) + "\n"
    text += "        - Prescale column: " + str(ps) + "\n"
    text += "        - Subsystems: " + str(ss) + "\n"
    text += "        - TRG subsystems: " + str(tss) + "\n"
    return text

def RunCAdd(time, text):
    return '\n' + TTAdd(time, text, 1)

def RateSAdd(phys, rand, tot, deadtime, strmphys, strmexp):

    pt = PrettyTable()
    pt.field_names = ["Rate", "Value"]
    pt.header = False
    pt.add_row(['Total L1A rate', rate_units(tot)])
    pt.add_row(['L1A physics', rate_units(phys)])
    pt.add_row(['L1A random', rate_units(rand)])
    pt.add_row(['Stream physics', rate_units(strmphys)])
    pt.add_row(['Stream express', rate_units(strmexp)])
    pt.add_row(['Dead time', str(deadtime) + " %"])
    pt.align = 'l'
    table_string = pt.get_string()
    table_string = '\n'.join('    ' + line for line in table_string.split('\n'))
    table_string += '\n'

    return table_string

def RunSAddNew(tkey, lhcstat, ss, tss):
    text = "    - Configuration: \n"
    text += "        - LHC status: " + str(lhcstat) + "\n"
    text += "        - Trigger Key: " + str(tkey) + "\n"
    text += "        - Subsystems: " + str(ss) + "\n"
    text += "        - TRG subsystems: " + str(tss) + "\n"
    return text

def RateSAddNew(auth, runnr, lsnr, ps):
    pt = PrettyTable()
    pt.field_names = ["Rate", "Value"]
    pt.header = False

    # Make calls to OMS to get the rates based on run and LS
    fieldsL1tRateQuery = "l1a_total,l1a_physics,l1a_random"
    omsL1tRateQuery = f"https://cmsoms.cern.ch/agg/api/v1/l1triggerrates?"
    omsL1tRateQuery += f"page[offset]=0&"
    omsL1tRateQuery += f"page[limit]=1&"
    omsL1tRateQuery += f"filter[run_number][EQ]={runnr}&"
    omsL1tRateQuery += f"filter[last_lumisection_number][EQ]={lsnr}&"
    omsL1tRateQuery += f"group[granularity]=lumisection&"
    omsL1tRateQuery += f"fields={fieldsL1tRateQuery}&"
    omsL1tRateQuery += f"sort=-lumisection_number"
    
    omsL1tRateRequest = requests.get(omsL1tRateQuery, **auth.authparams(), verify=False)
    orl1tq = omsL1tRateRequest.json()

    tot = orl1tq['data'][0]['attributes']['l1a_total']['rate']
    phys = orl1tq['data'][0]['attributes']['l1a_physics']['rate']
    rand = orl1tq['data'][0]['attributes']['l1a_random']['rate']

    fieldsStreamRateQuery = "stream_name,rate"
    omsStreamRateQuery = f"https://cmsoms.cern.ch/agg/api/v1/streams?"
    omsStreamRateQuery += f"page[offset]=0&"
    omsStreamRateQuery += f"page[limit]=100&"
    omsStreamRateQuery += f"filter[run_number][EQ]={runnr}&"
    omsStreamRateQuery += f"filter[last_lumisection_number][EQ]={lsnr}&"
    omsStreamRateQuery += f"group[granularity]=lumisection&"
    omsStreamRateQuery += f"fields={fieldsStreamRateQuery}&"
    omsStreamRateQuery += f"sort=-lumisection_number"

    omsStreamRateRequest = requests.get(omsStreamRateQuery, **auth.authparams(), verify=False)
    strmphys = 0
    strmexp = 0
    osrq = omsStreamRateRequest.json()
    for streams in osrq['data']:
        if "Express" in streams['attributes']['stream_name']:
            strmexp += streams['attributes']['rate']
        if streams['attributes']['stream_name'].startswith("Physics"):
            strmphys += streams['attributes']['rate']

    fieldsDeadtimeQuery = "overall_total_deadtime"
    omsDTQuery = f"https://cmsoms.cern.ch/agg/api/v1/deadtimes?"
    omsDTQuery += f"fields={fieldsDeadtimeQuery}&"
    omsDTQuery += f"page[offset]=0&page[limit]=1&"
    omsDTQuery += f"filter[run_number][EQ]={runnr}&"
    omsDTQuery += f"filter[first_lumisection_number][EQ]={lsnr}&"
    omsDTQuery += f"sort=-first_lumisection_number&"
    omsDTQuery += f"include=meta,presentation_timestamp&"
    omsDTQuery += f"group[granularity]=lumisection"

    omsDTRequest = requests.get(omsDTQuery, **auth.authparams(), verify=False)
    odtq = omsDTRequest.json()
    deadtime = odtq['data'][0]['attributes']['overall_total_deadtime']['percent']

    pt.add_row(['Total L1A rate', rate_units(tot)])
    pt.add_row(['L1A physics', rate_units(phys)])
    pt.add_row(['L1A random', rate_units(rand)])
    pt.add_row(['Stream physics', rate_units(strmphys)])
    pt.add_row(['Stream express', rate_units(strmexp)])
    pt.add_row(['Dead time', str(deadtime) + " %"])
    pt.align = 'l'
    table_string = pt.get_string()
    table_string = '\n'.join('    ' + line for line in table_string.split('\n'))
    table_string += '\n'

    out_string = "        - Prescale column: " + str(ps) + "\n"
    out_string += table_string
    return out_string

def AddNewRun(runnr, auth, cmnt):

    print('Gathering OMS query data for run ' + str(runnr) + '...')

    fieldsRunQuery = "start_time,end_time,l1_hlt_mode_stripped"
    omsRunQuery = f"https://cmsoms.cern.ch/agg/api/v1/runs?"
    omsRunQuery += f"page[offset]=0&"
    omsRunQuery += f"page[limit]=1&"
    omsRunQuery += f"filter[sequence][EQ]=GLOBAL-RUN&"
    omsRunQuery += f"filter[run_number][EQ]={runnr}&"
    omsRunQuery += f"fields={fieldsRunQuery}&"
    omsRunQuery += f"sort=-run_number"
    
    omsRunRequest = requests.get(omsRunQuery, **auth.authparams(), verify=False)
    orq = omsRunRequest.json()

    stime = orq['data'][0]['attributes']['start_time']
    stimeHM = re.findall(r'\d{2}:\d{2}', stime)[0]
    stimeHM = utc_to_local(stimeHM)
    etime = orq['data'][0]['attributes']['end_time']
    etime = etime if etime is not None else '[21:00]'
    etimeHM = re.findall(r'\d{2}:\d{2}', etime)[0]
    etimeHM = utc_to_local(etimeHM)
    tkey = orq['data'][0]['attributes']['l1_hlt_mode_stripped']
    lhcstat = cmnt['lhcstatus']
    ss = cmnt['subsystems']
    tss = cmnt['trgsubsystems']

    runelogtext = BR(stimeHM, runnr, cmnt['summary'])
    runelogtext += RunSAddNew(tkey, lhcstat, ss, tss)

    for item in cmnt['measure_rate']:
        runelogtext += RunCAdd(item['time'], item['text'])
        runelogtext += RateSAddNew(auth, runnr, item['lsnr'], item['ps'])

    runelogtext += ER(etimeHM, runnr)

    return runelogtext

def rate_units(inval):
    if inval < 1e3:
        return str(round(inval, 2)) + ' Hz'
    elif inval < 1e6:
        return str(round(inval, 0)/1e3) + ' kHz'
    else:
        return str(round(inval, 0)/1e6) + ' MHz'
    
def utc_to_local(t):
    h = int(t.split(':')[0])
    h = h+2
    if h >= 24:
        h = h - 24
    return str(h) + ':' + t.split(':')[1]