from prettytable import PrettyTable
from GenerateElog import TTAdd, TAdd, BR, ER, RunSAdd, RateSAdd, RunCAdd

with open("24_04_17_TRGShifter_Elog.txt", "w") as f:

    ptshiftsum = PrettyTable()
    ptshiftsum.field_names = ["Time From", "Time To", "Run Number", "Summary"]
    ptshiftsum.add_row(['Prev', '07:08', '379530', '1800b Fill 9530. Beam dumed as shift started.'])
    ptshiftsum.add_row(['07:15', '07:39', '379532', 'Cosmics. No HCAL.'])
    ptshiftsum.add_row(['07:42', '08:11', '379533', 'Cosmics. No HCAL, GEM.'])
    ptshiftsum.add_row(['08:24', '08:39', '379538', 'Cosmics. No HCAL, GEM, RPC.'])
    ptshiftsum.add_row(['09:23', '09:25', '379543', 'Cosmics. CSC only.'])
    ptshiftsum.add_row(['09:27', '09:41', '379544', 'Cosmics. CSC only. No TWINMUX.'])
    ptshiftsum.add_row(['09:44', '10:20', '379546', 'Cosmics. No TWINMUX, EMTF.'])
    ptshiftsum.add_row(['10:22', '10:54', '379548', 'Cosmics. No TWINMUX, EMTF.'])
    f.write(ptshiftsum.get_string() + '\n\n\n')

    f.write(TTAdd('06:54', "Morning shift started."))
    f.write(TAdd('Ongoing Run 379530', 1))

    # ====================================
    f.write(BR('Previous Shift', 379530))
    f.write(RunSAdd('l1_hlt_collisions2024/v71',
                    '4 - 2p0E34+ZeroBias+HLTPhysics',
                    'Proton Physics: Stable Beams',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('96.7 k', '382 ', '114 k', 4, '4 k', '720 '))

    f.write(RunCAdd('14:00', 'Change to prescale column 6.'))

    f.write(RunSAdd('l1_hlt_collisions2024/v71',
                    '6 - 2p0E34+HLTPhysics',
                    'Proton Physics: Stable Beams',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('68.5 k', '382 ', '68.9 k', 3, '3.5 k', '500 '))

    f.write('\n')
    f.write(TTAdd('06:59', "Beam dump warning received.\n"))

    f.write(RunCAdd('07:04', 'Change back to default prescale column.'))
    f.write(RunSAdd('l1_hlt_collisions2024/v71',
                    '4 - 2p0E34+ZeroBias+HLTPhysics',
                    'Proton Physics: Stable Beams',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('96.7 k', '382 ', '114 k', 4, '4 k', '720 '))

    f.write('\n')
    f.write(TTAdd('07:06', "Beam mode changed to beam dump."))
    f.write(TTAdd('07:06', "Beam mode changed to ramp down.\n"))

    f.write(ER('07:08', 379530))
    # ====================================

    # ====================================
    f.write(BR('07:15', 379532))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: Ramp Down',
                    'all except HCAL',
                    'all'
    ))
    f.write(RateSAdd('364 ', '113.8 k', '114 k', 5, '388 ', '388 '))

    f.write(RunCAdd('07:25', 'The cosmic express rate is too high. Change to prescale column 6.'))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '6 - HighRandom+Express',
                    'Proton Physics: Ramp Down',
                    'all except HCAL',
                    'all'
    ))
    f.write(RateSAdd('364 ', '113.8 k', '114 k', 5, '367 ', '124 '))
    f.write(ER('07:39', 379532))
    # ====================================

    # ====================================
    f.write(BR('07:42', 379533))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: Ramp Down',
                    'all except HCAL and GEM',
                    'all'
    ))
    f.write(RateSAdd('314 ', '113.8 k', '114 k', 5, '324 ', '324 '))

    f.write(RunCAdd('07:42', 'The cosmic express rate is too high. Change to prescale column 6.'))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '6 - HighRandom+Express',
                    'Proton Physics: Ramp Down',
                    'all except HCAL and GEM',
                    'all'
    ))
    f.write(RateSAdd('314 ', '113.8 k', '114 k', 5, '320 ', '107 '))

    f.write('\n')
    f.write(TTAdd('07:06', "Beam mode changed to no beam."))

    f.write(ER('08:11', 379533))
    # ====================================

    # ====================================
    f.write(BR('08:24', 379538))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'all except HCAL, GEM and RPC',
                    'all'
    ))
    f.write(RateSAdd('270 ', '114 k', '114.5 k', 4.9, '270 ', '270 '))

    f.write(RunCAdd('08:25', 'The cosmic express rate is too high. Change to prescale column 6.'))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '6 - HighRandom+Express',
                    'Proton Physics: No Beam',
                    'all except HCAL, GEM and RPC',
                    'all'
    ))
    f.write(RateSAdd('314 ', '113.8 k', '114 k', 5, '270 ', '96 '))

    f.write(ER('08:39', 379538))
    # ====================================

    # ====================================
    f.write(BR('09:23', 379543))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'CSC only',
                    'all'
    ))
    f.write(TAdd('\n', 1))
    f.write(TAdd('No data recorded.', 1))

    f.write(ER('09:25', 379543))
    # ====================================

    # ====================================
    f.write(BR('09:27', 379544))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'CSC only',
                    'all expect TWINMUX'
    ))
    f.write(RateSAdd('139 ', '114 k', '114 k', 5, '150 ', '150 '))

    f.write(ER('09:41', 379544))
    # ====================================

    # ====================================
    f.write(BR('09:44', 379546))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'none',
                    'all expect TWINMUX and EMTF'
    ))
    f.write(RateSAdd('0 ', '113.9 k', '114 k', 5, '12 ', '12 '))

    f.write(ER('10:20', 379544))
    # ====================================

    # ====================================
    f.write(BR('10:22', 379548))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'none',
                    'all expect TWINMUX and EMTF'
    ))
    f.write(RateSAdd('0 ', '113.9 k', '114 k', 5, '12 ', '12 '))

    f.write(ER('10:54', 379548))
    # ====================================

    f.write('\n')
    f.write(TTAdd('11:15', "Trigger shift system RAM capacity increased from 8 GB to 16 GB."))

    f.write(TAdd('Comment bla.', 1))
    f.write(TAdd('Maybe summarise the day plans.', 1))
    f.write(TAdd('Any major problems faced and if anything specific to look forward to.', 1))
    f.write(TTAdd('XX:XX', "Morning shift ended."))
