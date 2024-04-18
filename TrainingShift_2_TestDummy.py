from prettytable import PrettyTable
from GenerateElog import AddNewRun, TTAdd, TAdd

with open("24_04_17_TRGShifter_Elog_DummyTest.txt", "w") as f:

    ptshiftsum = PrettyTable()
    ptshiftsum.field_names = ["Time From", "Time To", "Run Number", "Summary"]
    ptshiftsum.add_row(['Prev', '07:08', '379530', '1800b Fill 9530. Beam dumed as shift started.'])
    ptshiftsum.add_row(['07:15', '07:39', '379532', 'Cosmics. No HCAL.'])
    f.write(ptshiftsum.get_string() + '\n\n\n')

    f.write(TTAdd('06:54', "Morning shift started."))
    f.write(TAdd('Ongoing Run 379530', 1))
    
    f.write(AddNewRun(379530, {'lhcstatus': 'Proton Physics: Stable Beams',
                                 'subsystems': 'all',
                                 'trgsubsystems': 'all',
                                 'measure_rate': 
                                 [{'time': '06:55', 'text': 'Rate at start of Run.', 
                                   'lsnr': '', 'ps': '4 - 2p0E34+ZeroBias+HLTPhysics'},
                                  {'time': '4 k', 'text': '720 ', 'ps': '4 k'}]
     }))