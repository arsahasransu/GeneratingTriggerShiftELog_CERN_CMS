from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import tsgauth

with open("24_04_17_TRGShifter_Elog_DummyTest.txt", "w") as f:

  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)


  ptshiftsum = PrettyTable()
  ptshiftsum.field_names = ["Time From", "Time To", "Run Number", "Summary"]
  ptshiftsum.add_row(['Prev', '07:08', '379530', '1800b Fill 9530. Beam dumed as shift started.'])
  ptshiftsum.add_row(['07:15', '07:39', '379532', 'Cosmics. No HCAL.'])
  
  f.write(ptshiftsum.get_string() + '\n\n\n')

  f.write(TTAdd('06:54', "Morning shift started."))
  f.write(TAdd('Ongoing Run 379530', 1))
    
  f.write(AddNewRun(379530, auth, 
                    {'lhcstatus': 'Proton Physics: Stable Beams',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '06:55', 'text': 'Rate at start of Run.',
                       'lsnr': '331', 'ps': '4 - 2p0E34+ZeroBias+HLTPhysics'}]
    }))
    
  f.write(TAdd('Systems taken to local. All except TRG systems Calo L1 and Calo L2 put back.', 1))
  f.write(TAdd('New TRG keys tested. Maybe expect more TRG keys.', 1))
  f.write(TAdd('Proton beams cycling. Expect collisions later today.', 1))
  f.write(TAdd('All TRG systems functioned nominal. Rates were as expected.', 1))
  f.write(TTAdd('14:56', "Morning shift ended."))
