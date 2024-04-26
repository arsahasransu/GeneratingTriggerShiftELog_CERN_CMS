from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import re
import tsgauth

with open("Elog_TRG_Shift_240424_1500to2300.txt", "w") as f:

  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

  el = [
    TTAdd('15:00', "Afternoon shift started."),
    TAdd('Ongoing Run 379926', 1),
    TAdd('HOM instruction to run with 1p8E34 PS column for 1200b to 2200b.', 1),
    TAdd('Default PS to still be 2p0E34 for 1200b to 2200b.', 2),
    TAdd('Instruction updated on L1T and HLT operation pages.', 2),
    
    AddNewRun(379926, auth, 
                    {'summary': 'Cosmics menu. No DT and GEM, no TWINMUX',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except DT and GEM',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '15:30', 'text': 'Rate at run transfer to afternoon shift.',
                       'lsnr': '132', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379931, auth, 
                    {'summary': 'Cosmics menu. No DT and GEM, no TWINMUX',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except DT and GEM',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '15:42', 'text': 'Rate at run start.',
                       'lsnr': '8', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379933, auth, 
                    {'summary': 'Cosmics menu. No DT and GEM, no TWINMUX',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except DT and GEM',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '15:52', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379937, auth, 
                    {'summary': 'L1Scout test. No GEM. Observed persistent TWINMUX error',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '16:49', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '4 - HighRandom'}
                     ],
    }),

    TTAdd('16:55', "Observed persistent error from RPC input ports in TWINMUX boards\n"),
    TAdd('Reported to shift leader, L1 DOC and shared screenshots on mattermost.', 1),
    TAdd('L1 DOC advised to contact DT DOC. DT DOC has taken system to local for testing.', 1),

    AddNewRun(379938, auth, 
                    {'summary': 'L1Scout test. No GEM. Observed persistent TWINMUX error',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '16:53', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '6 - HighRandom+Express'}
                     ],
    }),

    AddNewRun(379939, auth, 
                    {'summary': 'L1Scout test. Ignore Run. 2 LS only',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': [],
    }),

    AddNewRun(379940, auth, 
                    {'summary': 'L1Scout test. No GEM. Observed persistent TWINMUX error',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '17:03', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '6 - HighRandom+Express'}
                     ],
    }),

    AddNewRun(379941, auth, 
                    {'summary': 'L1Scout test. Observed persistent increase deadtime mid-run',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '17:24', 'text': 'Rate at run start.',
                       'lsnr': '30', 'ps': '4 - HighRandom'}
                     ],
    }),

    TTAdd('17:33', "High deadtime > 7%.\n"),
    TAdd('Reported to shift leader. L1 DOC contacted - Unavailable for 10 min.', 1),

    TTAdd('17:40', "Stop Run, Red-recycle trigger to attempt to fix deadtime. \n"),
    TAdd('Based on similar situation earlier today.', 1),

    AddNewRun(379943, auth, 
                    {'summary': 'L1Scout test. No DT and GEM, no TWINMUX',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '17:47', 'text': 'Rate at run start.',
                       'lsnr': '13', 'ps': '4 - HighRandom'}
                     ],
    }),

    TTAdd('17:51', "L1 DOC is on the deadtime issue. \n"),
    TTAdd('17:59', "L1 DOC suggested red-recycle trigger and temporarily reduce random rate by 5% to fix deadtime issue. \n"),
    TAdd('If problem occurs again, retry the above solution.', 1),

    AddNewRun(379945, auth, 
                    {'summary': 'L1Scout test. Deadtime issue fixed',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '17:58', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379946, auth, 
                    {'summary': 'L1Scout test',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': [],
    }),

    AddNewRun(379947, auth, 
                    {'summary': 'L1Scout test. No DT and GEM, no TWINMUX',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '18:08', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379948, auth, 
                    {'summary': 'L1Scout test. DAQ error. Run aborted',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '18:14', 'text': 'Rate at run start.',
                       'lsnr': '6', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379949, auth, 
                    {'summary': 'L1Scout test. Not sensible rates',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': [],
    }),

    AddNewRun(379950, auth, 
                    {'summary': 'Cosmics',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '18:32', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379950, auth, 
                    {'summary': 'Cosmics',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': 
                     [{'time': '18:32', 'text': 'Rate at run start.',
                       'lsnr': '4', 'ps': '4 - HighRandom'}
                     ],
    }),

    AddNewRun(379952, auth, 
                    {'summary': 'Testing. TWINMUX error not fixed',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM',
                     'trgsubsystems': 'all',
                     'measure_rate': [],
    }),

    AddNewRun(379953, auth, 
                    {'summary': 'DAQ FED error. Deadtime ~ 100%. Run aborted',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all except GEM and DT',
                     'trgsubsystems': 'all except TWINMUX',
                     'measure_rate': [],
    }),

    AddNewRun(379954, auth, 
                    {'summary': 'Cosmics. Observed high stream rate with DQMEventDisplay. DAQ error mid-run.',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '19:28', 'text': 'Rate at run start.',
                       'lsnr': '3', 'ps': '4 - HighRandom'},
                      {'time': '19:31', 'text': 'High express rate. Change to PS column 6',
                       'lsnr': '11', 'ps': '6 - HighRandom+Express'}
                     ],
    }),

    TTAdd('19:30', "Reported high stream rate with DQMEventDisplay to HOM. \n"),
    TAdd('Not inherently problematic. To be fixed by HOM in next trigger menu.', 1),

    AddNewRun(379955, auth, 
                    {'summary': 'Cosmics. Observed high stream rate with DQMEventDisplay. DAQ error mid-run.',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '20:17', 'text': 'Rate at run start.',
                       'lsnr': '7', 'ps': '6 - HighRandom+Express'},
                       {'time': '20:37', 'text': 'DAQ FED Error. Deadtime ~ 100%. Run aborted.',
                       'lsnr': '57', 'ps': '6 - HighRandom+Express'}
                     ],
    }),

    AddNewRun(379956, auth, 
                    {'summary': 'Cosmics. Observed high stream rate with DQMEventDisplay',
                     'lhcstatus': 'Proton Physics: No Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': 
                     [{'time': '20:45', 'text': 'Rate at run start.',
                       'lsnr': '10', 'ps': '6 - HighRandom+Express'}
                     ],
    }),

    TAdd('Observed persistent TWINMUX error from failure of RPC input port \n \
         when DT was put to global from local.', 1),
    TAdd('Observed increased deadtime to > 7%. Likely a result of some test. ', 1),
    TAdd('High stream rate with DQMEventDisplay observed with 120 kHz random \
         cosmics. Reported to HOM. To be fixed in next trigger menu.', 1),
    TAdd('System running nominal expect for the non-malicious high DQMEventDisplay\
         stream rate warning since Run 379954.', 1),
    TAdd('Expect 1419b collisons during night shift.', 1),
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

  
