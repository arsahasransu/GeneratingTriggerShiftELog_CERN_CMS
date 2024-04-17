from prettytable import PrettyTable
from GenerateElog import TTAdd, TAdd, BR, ER, RunSAdd, RateSAdd, RunCAdd

with open("Elog.txt", "w") as f:

    ptshiftsum = PrettyTable()
    ptshiftsum.field_names = ["Time From", "Time To", "Run Number", "Summary"]
    ptshiftsum.add_row(['13:04', '13:25', '379471', 'Comment 1'])
    ptshiftsum.add_row(['13:45', '14:20', '379472', 'Comment 2'])
    ptshiftsum.add_row(['14:40', '15:15', '379473', 'Comment 3'])
    f.write(ptshiftsum.get_string() + '\n\n\n')

    f.write(TTAdd('13:00', "Afternoon shift started."))
    f.write(TAdd('Comment 1 from previous shift', 1))
    f.write(TAdd('Comment 2 from previous shift', 1))
    f.write(TAdd('Comment 3 from previous shift', 1))

    # ====================================
    f.write(BR('13:04', 379471))
    f.write(RunSAdd('l1_hlt_cosmics2024/v73',
                    '4 - HighRandom',
                    'Proton Physics: Flat Top',
                    'all except EMTF',
                    'all except CSC and GEM'
    ))
    f.write(RateSAdd('67 ', '113.8 k', '114 k', 5, '80', '12'))

    f.write(RunCAdd('13:15', 'Comment indent with run.'))
    f.write(RunSAdd('l1_hlt_cosmics2024/v73',
                    '4 - HighRandom',
                    'Proton Physics: Flat Top',
                    'all except EMTF',
                    'all except CSC and GEM'
    ))
    f.write(RateSAdd('67 ', '113.8 k', '114 k', 5, '80', '12'))
    f.write(ER('13:25', 379471))
    # ====================================

    f.write('\n')
    f.write(TTAdd('13:30', "Some general comment outside run."))

    # ====================================
    f.write(BR('13:45', 379472))
    f.write(RunSAdd('l1_hlt_cosmics2024/v73',
                    '4 - HighRandom',
                    'Proton Physics: Flat Top',
                    'all except EMTF',
                    'all except CSC and GEM'
    ))
    f.write(RateSAdd('67 ', '113.8 k', '114 k', 5, '80', '12'))

    f.write(RunCAdd('14:00', 'Comment indent with run.'))
    f.write(TAdd('More details with run.', 2))
    f.write(RunSAdd('l1_hlt_cosmics2024/v73',
                    '4 - HighRandom',
                    'Proton Physics: Flat Top',
                    'all except EMTF',
                    'all except CSC and GEM'
    ))
    f.write(RateSAdd('67 ', '113.8 k', '114 k', 5, '80', '12'))
    f.write(ER('14:20', 379472))
    # ====================================

    # ====================================
    f.write(BR('14:40', 379473))
    f.write(RunSAdd('l1_hlt_cosmics2024/v73',
                    '4 - HighRandom',
                    'Proton Physics: Flat Top',
                    'all except EMTF',
                    'all except CSC and GEM'
    ))
    f.write(RateSAdd('67 ', '113.8 k', '114 k', 5, '80', '12'))

    f.write('\n')
    f.write(TTAdd('14:50', "Some general comment inside run.\n"))

    f.write(RunCAdd('14:55', 'Comment indent with run.'))
    f.write(TAdd('More details with run.', 2))
    f.write(RunSAdd('l1_hlt_cosmics2024/v73',
                    '4 - HighRandom',
                    'Proton Physics: Flat Top',
                    'all except EMTF',
                    'all except CSC and GEM'
    ))
    f.write(RateSAdd('67 ', '113.8 k', '114 k', 5, '80', '12'))
    f.write(ER('15:15', 379473))
    # ====================================

    f.write(TAdd('Comment with further info for the next shifter.', 1))
    f.write(TAdd('Maybe summarise the day plans.', 1))
    f.write(TAdd('Any major problems faced and if anything specific to look forward to.', 1))
    f.write(TTAdd('16:00', "Afternoon shift ended."))
