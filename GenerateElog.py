from prettytable import PrettyTable

def TTAdd(time, text, indent=0):
    return "    "*indent + "[" + time + "] " +  text + "\n"

def TAdd(text, indent=0):
    return "    "*(indent+1) + "- " + text + "\n"

def BR(time, run):
    text = "\n====================================\n"
    text += TTAdd(time, "Run " + str(run) + " started.\n\n")
    return text

def ER(time, run):
    text = '\n'
    text += TTAdd(time, "Run " + str(run) + " stopped.")
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

def RateSAdd(phys, rand, tot, deadtime, strmphys, strmexp):
    pt = PrettyTable()
    pt.field_names = ["Rate", "Value"]
    pt.header = False
    pt.add_row(['Total L1A rate', str(tot) + "Hz"])
    pt.add_row(['L1A physics', str(phys) + "Hz"])
    pt.add_row(['L1A random', str(rand) + "Hz"])
    pt.add_row(['Stream physics', str(strmphys) +"Hz"])
    pt.add_row(['Stream express', str(strmexp) + "Hz"])
    pt.add_row(['Dead time', str(deadtime) + " %"])
    pt.align = 'l'
    table_string = pt.get_string()
    table_string = '\n'.join('    ' + line for line in table_string.split('\n'))
    table_string += '\n'
    return table_string

def RunCAdd(time, text):
    return '\n' + TTAdd(time, text, 1)

