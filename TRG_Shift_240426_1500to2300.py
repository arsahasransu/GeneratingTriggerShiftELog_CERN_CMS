from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

import re
import tsgauth
import urllib3

with open("Elog_TRG_Shift_240426_1500to2300.txt", "w") as f:

  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)

  el = [
    TTAdd('15:00', "Afternoon shift started."),
    TAdd('Ongoing Run 380025', 1),
    TAdd('Run handed over from Morning shift.', 1),
    TAdd('Expecting stable collisions with 2200b. Probe beam ongoing', 1),
    
    TTAdd('15:10', "Beam status changed to INJECTION PHYSICS BEAM."),

    AddNewRun(380025, auth, 
                    {'summary': 'Circulating menu. Expecting 2200b collisions next.',
                     'lhcstatus': 'Proton Physics: Injection Probe Beam',
                     'subsystems': 'all except CSC',
                     'trgsubsystems': 'all except EMTF',
                     'measure_rate': 
                     [{'time': '14:55', 'text': 'Rate at run transfer to afternoon shift',
                       'lsnr': '17', 'ps': '11 - VHighBPTX'},
                       {'time': '14:56', 'text': 'PS column changed to 10 due to low rate',
                       'lsnr': '20', 'ps': '10 - HighBPTX'},
                       {'time': '14:59', 'text': 'PS column changed to 9 due to low rate',
                       'lsnr': '28', 'ps': '9 - MediumBPTX'},
                       {'time': '15:13', 'text': 'High rate from beam intensity increase',
                       'lsnr': '64', 'ps': '9 - MediumBPTX'},
                       {'time': '15:15', 'text': 'PS column changed to 10 due to high rate',
                       'lsnr': '68', 'ps': '10 - HighBPTX'},
                       {'time': '15:23', 'text': 'High rate from beam intensity increase',
                       'lsnr': '88', 'ps': '10 - HighBPTX'},
                       {'time': '15:25', 'text': 'PS column changed to 11 due to high rate',
                       'lsnr': '93', 'ps': '11 - VHighBPTX'}
                     ],
    }),

    AddNewRun(380026, auth, 
                    {'summary': 'Test new collision key. No T0',
                     'lhcstatus': 'Proton Physics: Injection Physics Beam',
                     'subsystems': 'all except CSC',
                     'trgsubsystems': 'all except EMTF',
                     'measure_rate': []
    }),

    AddNewRun(380027, auth, 
                    {'summary': 'Circulating menu',
                     'lhcstatus': 'Proton Physics: Injection Physics Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '15:39', 'text': 'Rate at run start',
                       'lsnr': '5', 'ps': '11 - VHighBPTX'},
                       {'time': '16:12', 'text': 'High rate at run end from Beam intensity increase',
                       'lsnr': '90', 'ps': '11 - VHighBPTX'}
                       ]
    }),

    TTAdd('15:30', "Beam status changed to RAMP."),

    AddNewRun(380028, auth, 
                    {'summary': 'Circulating menu',
                     'lhcstatus': 'Proton Physics: Injection Physics Beam',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '15:39', 'text': 'Rate at run start',
                       'lsnr': '5', 'ps': '11 - VHighBPTX'},
                       {'time': '16:42', 'text': 'Rate at run end. Increase due to ramp',
                       'lsnr': '58', 'ps': '11 - VHighBPTX'}
                       ]
    }),

    TTAdd('15:44', "Beam status changed to FLAT TOP followed by SQUEEZE."),

    TTAdd('16:54', "Beam status changed to ADJUST."),

    TTAdd('17:00', "Beam status changed to STABLE BEAMS. EMMITANCE SCAN expected to begin."),

    AddNewRun(380029, auth, 
                    {'summary': 'Collisions at 2211b',
                     'lhcstatus': 'Proton Physics: Flat Top',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '16:49', 'text': 'Rate at run start',
                       'lsnr': '3', 'ps': '7 - 2p0E34'} ,
                       {'time': '17:19', 'text': 'Rate at stable PU = 35',
                       'lsnr': '79', 'ps': '7 - 2p0E34'} 
                       ]
    }),

    TTAdd('17:53', "Deadtime high. Reported to SL and L1 DOC. DAQ shifter reported possibility from\
          pre-shower."),
    TAdd('SL contacted ECAL DOC.', 1),
    TAdd('Fixed by pausing run and restarting run and other actions by DAQ shifter.', 1),

    TTAdd('17:55', "HOM instruction to keep PS column at 9 unless the HLT CPU usage >= 94%, or BRAM is in backlog (Monitored by DAQ)."),
    TAdd('If this happens (unlikely), change to prescale to 7 - 2p0E34.', 1),

    AddNewRun(380030, auth, 
                    {'summary': 'Collisions at 2211b. Mid-run auto stop with DAQ error',
                     'lhcstatus': 'Proton Physics: Stable Beams',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '17:38', 'text': 'Rate at run start',
                       'lsnr': '5', 'ps': '7 - 2p0E34'} ,
                       {'time': '17:47', 'text': 'Change PS column to 9 on HOM instruction',
                       'lsnr': '27', 'ps': '9 - 1p8E34'} ,
                       {'time': '17:54', 'text': 'Rate at PU 63. High deadtime reported by CSC.',
                       'lsnr': '44', 'ps': '9 - 1p8E34'} ,
                       {'time': '18:16', 'text': 'HOM instruction. Changed PS column from 9 to 6.',
                       'lsnr': '101', 'ps': '6 - 2p0E34+HLTPhysics'} ,
                       {'time': '18:28', 'text': 'HLT Physics collected for at least 25 LS. Change back to 6.',
                       'lsnr': '130', 'ps': '9 - 1p8E34'} 
                       ]
    }),

    AddNewRun(380031, auth, 
                    {'summary': 'Collisions at 2211b. Attempt restart run. Failure with DAQ error. No data taken',
                     'lhcstatus': 'Proton Physics: Stable Beams',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': []
    }),

    AddNewRun(380032, auth, 
                    {'summary': 'Collisions at 2211b. Restart run. Some tracker FED excluded. Run has many deadtime issues',
                     'lhcstatus': 'Proton Physics: Stable Beams',
                     'subsystems': 'all',
                     'trgsubsystems': 'all',
                     'measure_rate': [{'time': '20:27', 'text': 'Rate mid-run',
                       'lsnr': '40', 'ps': '9 - 1p8E34'}
                      ]
    }),

    TTAdd('21:46', "Beam status changed to DUMP followed by RAMP DOWN."),

    TTAdd('21:48', "Investigated Run 380032 for data quality due to missing TIB FED."),
    TAdd('TRG Shifter and trainee Jannicke Andree Pearkes (@jpearkes) identified triggers that might have lower rate due to missing FED', 1),
    TAdd('Comapred the rate v PU  plot on ratemon tool between Run 380030 and Run 380032 for this.', 1),
    TAdd('List of HLT paths that have been ideintified as having low rate.', 1),
    TAdd('HLT_PFScouting_DatasetMuon', 2),
    TAdd('HLT_PFMET120_PFMHT120_IDTight_PFHT60', 2),
    TAdd('DST_PFScouting_JetHT', 2),
    TAdd('HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless', 2),
    TAdd('HLT_HT200_L1SingleLLPJet_DisplacedDiJet40_Inclusive1PtrkShortSig5', 2),

    TAdd('Observed higher frequency of deadtime during Runs. Likely related to failing FEDs. But under investigation by experts now.', 1),
    TAdd('Special instruction from HOM. Also updated on L1T instruction page.', 1),
    TAdd('For runs with 2211b (as expected over the weekend), run with PS column 9 - 1p8E34', 2),
    TAdd('Keep a watch over HLT CPU usage. It should be < 94 % in usage', 2),
    TAdd('Ask the DAQ to keep an eye on the BRAM which should not have large backlog.', 2),
    TAdd('If any of the above happens, inform shift leader and switch to PS column 7 - 2p0E34', 2),

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

  
