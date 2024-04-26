from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import re
import tsgauth

with open("Elog_TRG_Shift_240425_1500to2300.txt", "w") as f:

  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

  el = [
    TTAdd('15:00', "Afternoon shift started."),
    TAdd('Ongoing Run 379984', 1),
    TAdd('Run handed over from Morning shift.', 1),
    TAdd('Stable collisions with 1419b ongoing.', 1),
    TAdd('PS column at 10. Instructions to run on this for 2 hours and change back to 9.', 1),
    
    AddNewRun(379984, auth, 
                    {'summary': '1419b collisions',
                     'lhcstatus': 'Proton Physics: Stable Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '15:45', 'text': 'Rate at run transfer to afternoon shift',
                       'lsnr': '337', 'ps': '10 - 1p8E34+ZeroBias'},
                       {'time': '16:42', 'text': 'HOM instruction. Collected Ephemeral. Revert to PS column 9.',
                       'lsnr': '475', 'ps': '9 - 1p8E34'},
                       {'time': '18:04', 'text': 'Natural rate degradation with time. Rate before lumi-levelling.',
                       'lsnr': '697', 'ps': '9 - 1p8E34'},
                       {'time': '18:38', 'text': 'beta* reduction. Lumi-levelling. Rate back to nominal levels.',
                       'lsnr': '777', 'ps': '9 - 1p8E34'}
                     ],
    }),

    TTAdd('19:39', "Beam dump warning received."),
    TTAdd('19:48', "Beam dumped. Ramp Down"),

    AddNewRun(379990, auth, 
                    {'summary': 'Trigger collisons key testing. No T0',
                     'lhcstatus': 'Proton Physics: Ramp down',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': []
    }),

    AddNewRun(379991, auth, 
                    {'summary': 'Trigger circulating key testing. No T0',
                     'lhcstatus': 'Proton Physics: Ramp down',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': []
    }),

    AddNewRun(379992, auth, 
                    {'summary': 'Trigger comsics key testing. No T0',
                     'lhcstatus': 'Proton Physics: Setup',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': []
    }),

    AddNewRun(379997, auth, 
                    {'summary': 'Circulating. Too short run to measure rate',
                     'lhcstatus': 'Proton Physics: Setup',
                     'subsystems': 'all except CSC',
                     'trgsubsystems': 'all except EMTF',
                     'measure_rate': []
    }),

    TTAdd('20:42', "Beam status changed to INJECTION PROBE BEAM."),
    TTAdd('21:03', "Beam status changed to INJECTION PHYSICS BEAM."),

    AddNewRun(379998, auth, 
                    {'summary': 'Circulating. Run stopped from DAQ error',
                     'lhcstatus': 'Proton Physics: Injection Probe Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '20:59', 'text': 'Rate at run start',
                       'lsnr': '3', 'ps': '11 - VHighBPTX'}
                      ]
    }),

    TTAdd('21:19', "Beam status changed to INJECTION PROBE BEAM."),
    TTAdd('21:25', "Beam status changed to INJECTION PHYSICS BEAM."),

    AddNewRun(379999, auth, 
                    {'summary': 'Circulating',
                     'lhcstatus': 'Proton Physics: Injection Probe Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '21:10', 'text': 'Rate at run start. Changed PS to 10 due to low physics rate.',
                       'lsnr': '10', 'ps': '10 - HighBPTX'},
                       {'time': '21:19', 'text': 'Lost beam',
                       'lsnr': '35', 'ps': '10 - HighBPTX'},
                       {'time': '21:21', 'text': 'Changed to PS column 9. Low stream physics rate',
                       'lsnr': '42', 'ps': '9 - MediumBPTX'},
                       {'time': '21:27', 'text': 'Rate increase from injection physics beam.',
                       'lsnr': '55', 'ps': '9 - MediumBPTX'},
                       {'time': '21:28', 'text': 'Change PS to 10 due to high stream physics rate.',
                       'lsnr': '58', 'ps': '10 - HighBPTX'},
                       {'time': '21:33', 'text': 'Change PS to 11 due to high stream physics rate.',
                       'lsnr': '70', 'ps': '11 - HighBPTX'}
                       ]
    }),

    AddNewRun(38000, auth, 
                    {'summary': 'Circulating',
                     'lhcstatus': 'Proton Physics: RAMP',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '22:11', 'text': 'Rate at run start.',
                       'lsnr': '10', 'ps': '11 - VHighBPTX'}
                       ]
    }),

    TTAdd('22:22', "Beam status changed to FLAT TOP followed by SQUEEZE."),
    TTAdd('22:30', "Beam status changed to ADJUST."),
    TTAdd('22:30', "Beam status changed to STABLE BEAMS."),

    AddNewRun(38001, auth, 
                    {'summary': 'Collisions. 1959 b',
                     'lhcstatus': 'Proton Physics: SQUEEZE',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '22:28', 'text': 'Rate at run start.',
                       'lsnr': '5', 'ps': '9 - 1p8E34'},
                       {'time': '22:35', 'text': 'Rate increase after adjust.',
                       'lsnr': '24', 'ps': '9 - 1p8E34'}
                       ]
    }),

    TAdd('Stable beam collisions with 2000b ongoing.', 1),
    TAdd('L1T and HLT rates are unusually low. Probably expected from emiitance scan which is ongoing.', 1),
    TAdd('Report to shift leader and L1 DOC, if the rate continues to be low. For reference check the rates in Run 379984 which was with 1200b.', 1),
    TAdd('No other changes expected. System was nominal throughout the shift.', 1),
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

  
