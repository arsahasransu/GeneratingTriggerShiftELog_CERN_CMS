from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import re
import tsgauth

with open("24_04_17_TRGShifter_Elog_DummyTest.txt", "w") as f:

  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

  el = [
    TTAdd('06:54', "Morning shift started."),
    TAdd('Ongoing Run 379530', 1),
    
    AddNewRun(379530, auth, 
                    {'summary': '1800b Fill 9530. Beam dumped as shift started.',
                     'lhcstatus': 'Proton Physics: Stable Beams',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '06:55', 'text': 'Rate at start of Run.',
                       'lsnr': '331', 'ps': '4 - 2p0E34+ZeroBias+HLTPhysics'},
                      {'time': '06:58', 'text': 'Change to prescale column 6.',
                       'lsnr': '616', 'ps': '6 - 2p0E34+HLTPhysics'},
                      {'time': '07:04', 'text': 'Change to prescale column 4.',
                       'lsnr': '627', 'ps': '4 - 2p0E34+ZeroBias+HLTPhysics'},
                       ]
    }),
    TTAdd('06:59', "Beam dump warning received.\n"),
    TTAdd('07:06', "Beam mode changed to beam dump."),
    TTAdd('07:06', "Beam mode changed to ramp down.\n"),

    AddNewRun(379532, auth,
                    {'summary': 'Cosmics. No HCAL',
                     'lhcstatus': 'Proton Physics: Ramp Down',
                     'subsystems': 'all except HCAL',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '06:55', 'text': 'Rate at start of Run.',
                       'lsnr': '4', 'ps': '4 - HighRandom'},
                       {'time': '07:25', 'text': 'The cosmic express rate is too high. Change to prescale column 6.',
                       'lsnr': '35', 'ps': '6 - Express'}
                     ]
    }),
    TAdd('Systems taken to local. All except TRG systems Calo L1 and Calo L2 put back.', 1),
    TAdd('New TRG keys tested. Maybe expect more TRG keys.', 1),
    TAdd('Proton beams cycling. Expect collisions later today.', 1),
    TAdd('All TRG systems functioned nominal. Rates were as expected.', 1),
    TTAdd('14:56', "Morning shift ended.")
  
  ]

  ptshiftsum = PrettyTable()
  ptshiftsum.field_names = ["Time From", "Time To", "Run Number", "Summary"]
  ptshiftsum.align['Summary'] = 'l'
  for line in el:
    start_pattern = r'\[(\d{1,2}:\d{2})\] Run (\d+) started: (.*?)\n'
    match = re.search(start_pattern, line)
    if match:
      stop_pattern = r'\[(\d{1,2}:\d{2})\] Run \d+ stopped'
      stop_match = re.search(stop_pattern, line)
      ptshiftsum.add_row([match.group(1), stop_match.group(1), 
                          match.group(2), match.group(3)])

    f.write(line)
  
  f.write('\n RUN SUMMARY DURING SHIFT\n')
  f.write(ptshiftsum.get_string() + '\n\n\n')

  