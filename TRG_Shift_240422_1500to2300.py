from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import re
import tsgauth

with open("Elog_TRG_Shift_240422_1500to2300.txt", "w") as f:

  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

  el = [
    TTAdd('15:10', "Afternoon shift started."),
    TAdd('Ongoing Run 379822', 1),
    TAdd('Expected cosmics until 8 pm. Cryo recovery in LHC.', 1),
    TAdd('LHC start expected at 1200b. So expect the TRG menu change to that for 1200 b.', 1),
    
    AddNewRun(379822, auth, 
                    {'summary': 'Cosmics. HCAL out. Continued from previous run',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except HCAL.',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '15:17', 'text': 'Rate at run transfer to afternoon shift.',
                       'lsnr': '140', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    AddNewRun(379826, auth, 
                    {'summary': 'Cosmics. HCAL out',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except HCAL.',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '17:11', 'text': 'Rate throughout run.',
                       'lsnr': '6', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    AddNewRun(379829, auth, 
                    {'summary': 'Good Cosmics. Abrupt system failure',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '16:31', 'text': 'Rate at run start.',
                       'lsnr': '5', 'ps': '4 - HighRandom'},
                      {'time': '18:34', 'text': 'L1 random increase to 115 kHz.',
                       'lsnr': '11', 'ps': '4 - HighRandom'},
                      {'time': '18:36', 'text': 'High Express rate. Prescale change to column 6.',
                       'lsnr': '17', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    AddNewRun(379830, auth, 
                    {'summary': 'Good Cosmics',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '18:42', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '4 - HighRandom'},
                      {'time': '18:44', 'text': 'High Express rate. Prescale change to column 6.',
                       'lsnr': '9', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    TTAdd('19:37', "Test trigger key for LHC run with upcoming 1200 b.\n"),

    AddNewRun(379831, auth, 
                    {'summary': 'Cosmics. Testing a new trigger key for 1200 b',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '19:41', 'text': 'Rate at run start.',
                       'lsnr': '8', 'ps': '7 - 2p0E34'},
                       ]
    }),

    TTAdd('19:42', "High data rate. Changed to prescale column 11. Data taking stopped before prescale change.\n"),

    AddNewRun(379836, auth, 
                    {'summary': 'Good Cosmics',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '19:54', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '4 - HighRandom'},
                      {'time': '19:55', 'text': 'High Express rate. Prescale change to column 6.',
                       'lsnr': '7', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    AddNewRun(379837, auth, 
                    {'summary': 'Cosmics. Testing a new trigger key for 1200 b. No T0 output',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '20:06', 'text': 'Rate at run start.',
                       'lsnr': '5', 'ps': '7 - 2p0E34'}
                       ]
    }),

    AddNewRun(379839, auth, 
                    {'summary': 'Good Cosmics. Abrupt system failure',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '20:18', 'text': 'Rate at run start.',
                       'lsnr': '6', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    AddNewRun(379840, auth, 
                    {'summary': 'Good Cosmics.',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '21:55', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '6 - HighRandom+Express'},
                       ]
    }),

    TAdd('During lumi-levelling with 1200 b stable collisions (default PS = 9), take 10 min of data with PS = 6.', 1),
    TAdd('HLT keys for 1200 b tested for single-beam test and stable collisions.', 1),
    TAdd('Cosmic runs only. Trigger rates as expected. System nominal.', 1),
    TTAdd('23:00', "Afternoon shift ended.")
  
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

  
