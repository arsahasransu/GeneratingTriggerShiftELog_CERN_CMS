import tsgauth
import requests

if __name__ == "__main__":

    auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

    runnr = 379530
    lsnr = 430

    fieldsRunQuery = "start_time,end_time,l1_hlt_mode_stripped,hlt_key"
    omsRunQuery = f"https://cmsoms.cern.ch/agg/api/v1/runs?"
    omsRunQuery += f"page[offset]=0&"
    omsRunQuery += f"page[limit]=1&"
    omsRunQuery += f"filter[sequence][EQ]=GLOBAL-RUN&"
    omsRunQuery += f"filter[run_number][EQ]={runnr}&"
    omsRunQuery += f"fields={fieldsRunQuery}&"
    omsRunQuery += f"sort=-run_number"
    
    omsRunRequest = requests.get(omsRunQuery, **auth.authparams(), verify=False)
    
    fieldsL1tRateQuery = "last_lumisection_number,l1a_total,l1a_physics,l1a_random"
    omsL1tRateQuery = f"https://cmsoms.cern.ch/agg/api/v1/l1triggerrates?"
    omsL1tRateQuery += f"page[offset]=0&"
    omsL1tRateQuery += f"page[limit]=1&"
    omsL1tRateQuery += f"filter[run_number][EQ]={runnr}&"
    omsL1tRateQuery += f"filter[last_lumisection_number][EQ]={lsnr}&"
    omsL1tRateQuery += f"group[granularity]=lumisection&"
    omsL1tRateQuery += f"fields={fieldsL1tRateQuery}&"
    omsL1tRateQuery += f"sort=-lumisection_number"
    
    omsL1tRateRequest = requests.get(omsL1tRateQuery, **auth.authparams(), verify=False)

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

    fieldsDeadtimeQuery = "overall_total_deadtime,beamactive_total_deadtime,first_lumisection_number"
    omsDTQuery = f"https://cmsoms.cern.ch/agg/api/v1/deadtimes?"
    omsDTQuery += f"fields={fieldsDeadtimeQuery}&"
    omsDTQuery += f"page[offset]=0&page[limit]=1&"
    omsDTQuery += f"filter[run_number][EQ]={runnr}&"
    omsDTQuery += f"filter[first_lumisection_number][EQ]={lsnr}&"
    omsDTQuery += f"sort=-first_lumisection_number&"
    omsDTQuery += f"include=meta,presentation_timestamp&"
    omsDTQuery += f"group[granularity]=lumisection"

    omsDTRequest = requests.get(omsDTQuery, **auth.authparams(), verify=False)

    orq = omsRunRequest.json()
    for k, v in orq['data'][0]['attributes'].items():
        print(f"{k}: {v}")

    orl1tq = omsL1tRateRequest.json()
    for k, v in orl1tq['data'][0]['attributes'].items():
        print(f"{k}: {v}")

    physics_rate = 0
    express_rate = 0
    osrq = omsStreamRateRequest.json()
    for streams in osrq['data']:
        if "Express" in streams['attributes']['stream_name']:
            express_rate += streams['attributes']['rate']
        if streams['attributes']['stream_name'].startswith("Physics"):
            physics_rate += streams['attributes']['rate']

    print(f"Physics rate: {physics_rate} Hz")
    print(f"Express rate: {express_rate} Hz")

    odtq = omsDTRequest.json()
    for k, v in odtq['data'][0]['attributes'].items():
        print(f"{k}: {v}")