from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import re
import tsgauth

with open("Elog_TRG_Shift_240423_1500to2300.txt", "w") as f:

  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

  el = [
    TTAdd('15:00', "Afternoon shift started."),
    TAdd('Ongoing Run 379856', 1),
    TAdd('LHC injecting physics beams.', 1),
    
    TTAdd('15:04', "Beam mode changed to INJECTION PROBE BEAM.\n"),
    TTAdd('17:00', "Beam mode changed to INJECTION PHYSICS BEAM.\n"),
    TTAdd('17:27', "Beam mode changed to INJECTION PROBE BEAM.\n"),
    TTAdd('17:30', "Beam mode changed to INJECTION PHYSICS BEAM.\n"),
    TTAdd('17:54', "Beam mode changed to PREPARE RAMP.\n"),
    TTAdd('17:59', "Beam mode changed to RAMP.\n"),

    AddNewRun(379856, auth, 
                    {'summary': 'Circulating menu. Continued from previous run',
                     'lhcstatus': 'Proton Physics: Injection Probe Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '15:07', 'text': 'Rate at run transfer to afternoon shift.',
                       'lsnr': '304', 'ps': '11 - VHighBPTX'},
                      {'time': '15:44', 'text': 'Low stream rate. Change to PS column 9',
                       'lsnr': '401', 'ps': '9 - MediumBPTX'},
                      {'time': '17:02', 'text': 'Rate post injection physics beam.',
                       'lsnr': '601', 'ps': '9 - MediumBPTX'},
                      {'time': '17:07', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '614', 'ps': '9 - MediumBPTX'},
                      {'time': '17:15', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '635', 'ps': '9 - MediumBPTX'},
                      {'time': '17:22', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '652', 'ps': '9 - MediumBPTX'},
                      {'time': '17:25', 
                       'text': 'Rate approaching suggested stream rate threshold.\
                          Change to higher PS column 10.',
                       'lsnr': '660', 'ps': '10 - HighBPTX'},
                      {'time': '17:28', 'text': 'Rate post injection probe beam.',
                       'lsnr': '670', 'ps': '10 - HighBPTX'},
                      {'time': '17:30', 'text': 'Low stream rate. Change to PS column 9.',
                       'lsnr': '675', 'ps': '9 - MediumBPTX'},
                      {'time': '17:35', 'text': 'Rate post injection physics beam.',
                       'lsnr': '685', 'ps': '9 - MediumBPTX'},
                      {'time': '17:37', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '691', 'ps': '9 - MediumBPTX'},
                      {'time': '17:38', 'text': 'High stream rate. Changing PS column to 10.',
                       'lsnr': '694', 'ps': '10 - HighBPTX'},
                      {'time': '17:40', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '697', 'ps': '10 - HighBPTX'},
                      {'time': '17:46', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '715', 'ps': '10 - HighBPTX'},
                      {'time': '17:48', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '722', 'ps': '10 - HighBPTX'},
                      {'time': '17:51', 'text': 'Beam ramp up. Rate increase.',
                       'lsnr': '727', 'ps': '10 - HighBPTX'},
                      {'time': '17:53', 'text': 'High stream rate. Changing PS column to 11.',
                       'lsnr': '732', 'ps': '11 - VHighBPTX'}
                      ]
    }),

    AddNewRun(379857, auth, 
                    {'summary': 'Circulating menu. Mid run error in DAQ',
                     'lhcstatus': 'Proton Physics: Ramp',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '18:00', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '11 - VHighBPTX'}
                     ]
      }),

    AddNewRun(379859, auth, 
                    {'summary': 'Circulating menu before unstable collisions',
                     'lhcstatus': 'Proton Physics: Ramp',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '18:07', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '11 - VHighBPTX'},
                      {'time': '18:17', 
                       'text': 'Energy ramped upto 6 TeV. Increase in physics rate.',
                       'lsnr': '30', 'ps': '11 - VHighBPTX'}
                     ]
      }),

    TTAdd('18:20', "Beam mode changed to FLAT TOP. Ready for collision menu.\n"),
    TTAdd('18:30', "Beam mode changed to SQUEEZE.\n"),
    TTAdd('18:40', "Beam mode changed to ADJUST.\n"),
    TTAdd('20:23', "Beam DUMPED and changed to RAMP DOWN.\n"),

    AddNewRun(379862, auth, 
                    {'summary': 'Unstable collisions. PS changed to 0 midway',
                     'lhcstatus': 'Proton Physics: Flat Top',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '18:26', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '9 - 1p8e34'},
                      {'time': '18:35', 'text': 'Rate increase from beam squeeze.',
                       'lsnr': '25', 'ps': '9 - 1p8e34'},
                      {'time': '18:45', 'text': 'Rate increase from beam adjust.',
                       'lsnr': '50', 'ps': '9 - 1p8e34'},
                      {'time': '20:00', 
                      'text': 'Changed to PS column 0 following L1T instruction manual.',
                       'lsnr': '240', 'ps': '0 - Emergency'}
                     ]
      }),

    TTAdd('20:47', "Beam SETUP for 1200b physics.\n"),
    TTAdd('21:07', "Beam mode changed to INJECTION PROBE BEAM.\n"),

    AddNewRun(379863, auth, 
                    {'summary': 'Cosmics menu',
                     'lhcstatus': 'Proton Physics: Ramp Down',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '20:29', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '4 - HighRandom'},
                       {'time': '20:30', 'text': 'Change to PS column 6. High express rate.',
                       'lsnr': '7', 'ps': '6 - HighRandom+Express'},
                       {'time': '20:52', 'text': 'Muon systems switched to standby for collisions.\
                        Stream rates down by a significant factor.',
                       'lsnr': '60', 'ps': '6 - HighRandom+Express'},
                     ]
      }),

    TTAdd('21:18', "Beam mode changed to INJECTION PHYSICS BEAM.\n"),
    TTAdd('21:28', "Beam mode changed to INJECTION PROBE BEAM.\n"),
    TTAdd('21:28', "Beam mode changed to INJECTION PHYSICS BEAM.\n"),

    AddNewRun(379864, auth, 
                    {'summary': 'Circulating menu before 1200b physics collisions',
                     'lhcstatus': 'Proton Physics: Injection Probe Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '21:18', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '11 - VHighBPTX'},
                       {'time': '21:23', 'text': 'Change to PS column 9. Low stream rate.',
                       'lsnr': '16', 'ps': '9 - MediumBPTX'},
                       {'time': '21:26', 'text': 'Change to PS column 10. High stream rate.',
                       'lsnr': '22', 'ps': '10 - HighBPTX'},
                       {'time': '21:47', 'text': 'High stream rate from beam intensity increase.',
                       'lsnr': '77', 'ps': '10 - HighBPTX'},
                       {'time': '21:49', 'text': 'Change to PS column 9.',
                       'lsnr': '80', 'ps': '11 - VHighBPTX'},
                       {'time': '22:19', 'text': 'Rate before collisions',
                       'lsnr': '158', 'ps': '11 - VHighBPTX'}
                     ]
      }),

    AddNewRun(379866, auth, 
                    {'summary': 'Collisions menu. 1200b physics run. Handover to night shift.',
                     'lhcstatus': 'Proton Physics: Squeeze',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '22:29', 'text': 'Rate at run start.',
                       'lsnr': '6', 'ps': '9 - 1p8E34'}
                     ]
      }),

    TTAdd('22:21', "Beam mode changed to FLAT TOP.\n"),
    TTAdd('22:22', "Beam mode changed to SQUEEZE.\n"),

    TAdd('Ongoing 1200b physics run 379866. Hnaded over to night shift.', 1),
    TAdd('Expect PS column change to 6 - 2p0E34+HLTPhysics for 10 min during lumi-levelling\
          based on HOM instructions.', 1),
    TAdd('System nominal apart from ocassional warnings and errors.', 1),
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

  
