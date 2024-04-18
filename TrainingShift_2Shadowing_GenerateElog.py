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
    ptshiftsum.add_row(['10:22', '10:54', '379548', 'Cosmics. No TWINMUX, EMTF. Systems to local.'])
    ptshiftsum.add_row(['13:09', '13:21', '379572', 'Systems to global. Cosmics. With ECAL, DT, GEM. No EMTF.'])
    ptshiftsum.add_row(['13:24', '13:30', '379574', 'Cosmics. No RPC, CSC. No EMTF.'])
    ptshiftsum.add_row(['13:30', '13:41', '379575', 'Cosmics. No RPC. No EMTF.'])
    ptshiftsum.add_row(['13:43', '13:49', '379576', 'Start testing new TRG keys. Cosmics. All. No T0 output.'])
    ptshiftsum.add_row(['13:59', '14:01', '379580', 'Circulating. All. No T0 output. DAQ fail. '])
    ptshiftsum.add_row(['14:02', '14:04', '379581', 'Circulating. All. No T0 output. DAQ fail.'])
    ptshiftsum.add_row(['14:07', '14:11', '379582', 'Circulating. All. No T0 output.'])
    ptshiftsum.add_row(['14:14', '14:20', '379583', 'Collisions. All. No T0 output.'])
    ptshiftsum.add_row(['14:22', '14:27', '379584', 'LumiScan. All. No T0 output.'])
    ptshiftsum.add_row(['14:22', '14:53', '379585', 'Cosmics. All except CaloL1, CaloL2.'])
    ptshiftsum.align['Summary'] = 'l'
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
    f.write(TAdd('Run ended with DAQ error.', 1))
    f.write(TAdd('Too short for rate measurement.', 1))

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
    f.write(TTAdd('13:00', "Local systems are changed to Global to begin system-wide checks."))

    # ====================================
    f.write(BR('13:09', 379572))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'ECAL, DT and GEM only',
                    'all expect EMTF'
    ))
    f.write(RateSAdd('117 ', '113.8 k', '114 k', 5.1, '125 ', '125 '))

    f.write(ER('13:21', 379572))
    # ====================================

    # ====================================
    f.write(BR('13:24', 379574))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'all except RPC and CSC',
                    'all expect EMTF'
    ))
    f.write(RateSAdd('118 ', '113.8 k', '114 k', 5.1, '131 ', '125 '))

    f.write(ER('13:30', 379574))
    # ====================================

    # ====================================
    f.write(BR('13:30', 379575))
    f.write(RunSAdd('l1_hlt_cosmics2024/v76',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'all except RPC',
                    'all expect EMTF'
    ))
    f.write(RateSAdd('119 ', '113.8 k', '114 k', 5.1, '130 ', '125 '))

    f.write(ER('13:41', 379575))
    # ====================================

    f.write('\n')
    f.write(TTAdd('13:40', "Obtained the new trigger keys. Test the system with RPC in first before testing the new trigger keys."))

    # ====================================
    f.write(BR('13:43', 379576))
    f.write(RunSAdd('l1_hlt_cosmics2024/v77',
                    '4 - HighRandom',
                    'Proton Physics: No Beam',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('133 ', '113.8 k', '114 k', 5.1, '140 ', '131 '))
    f.write(TAdd('\n', 1))
    f.write(TAdd('No T0 output', 1))

    f.write(ER('13:49', 379576))
    # ====================================

    # ====================================
    f.write(BR('13:59', 379580))
    f.write(RunSAdd('l1_hlt_circulating2024/v49',
                    '11 - VHighBPTX',
                    'Proton Physics: No Beam',
                    'all',
                    'all'
    ))
    f.write(TAdd('\n', 1))
    f.write(TAdd('Run ended with DAQ error.', 1))
    f.write(TAdd('Too short for rate measurement.', 1))


    f.write(ER('14:01', 379580))
    # ====================================

    f.write('\n')
    f.write(TTAdd('14:00', "LHC proton beam status changed to cycling."))

    # ====================================
    f.write(BR('14:02', 379581))
    f.write(RunSAdd('l1_hlt_circulating2024/v49',
                    '11 - VHighBPTX',
                    'Proton Physics: Cycling',
                    'all',
                    'all'
    ))
    f.write(TAdd('\n', 1))
    f.write(TAdd('Run ended with DAQ error.', 1))
    f.write(TAdd('Too short for rate measurement.', 1))


    f.write(ER('14:04', 379581))
    # ====================================

    # ====================================
    f.write(BR('14:06', 379582))
    f.write(RunSAdd('l1_hlt_circulating2024/v49',
                    '11 - VHighBPTX',
                    'Proton Physics: Cycling',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('282 ', '400 ', '783 ', 1.23, '289 ', '289 '))
    f.write(TAdd('\n', 1))
    f.write(TAdd('No T0 output', 1))


    f.write(ER('14:11', 379582))
    # ====================================

    # ====================================
    f.write(BR('14:14', 379583))
    f.write(RunSAdd('l1_hlt_collisions2024/v72',
                    '7 - 2pE034',
                    'Proton Physics: Cycling',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('309 ', '400 ', '809 ', 1.23, '36 ', '409 '))
    f.write(TAdd('\n', 1))
    f.write(TAdd('No T0 output', 1))


    f.write(ER('14:20', 379583))
    # ====================================

    # ====================================
    f.write(BR('14:22', 379584))
    f.write(RunSAdd('l1_hlt_lumiscan/v10',
                    '4 - L1H6',
                    'Proton Physics: Cycling',
                    'all',
                    'all'
    ))
    f.write(RateSAdd('0 ', '397 ', '497 ', 1.25, '0.2 ', '4 '))
    f.write(TAdd('\n', 1))
    f.write(TAdd('No T0 output', 1))


    f.write(ER('14:27', 379584))
    # ====================================

    # ====================================
    f.write(BR('14:22', 379585))
    f.write(RunSAdd('l1_hlt_cosmics2024/v77',
                    '4 - HighRandom',
                    'Proton Physics: Cycling',
                    'all',
                    'all except CaloL1 and CaloL2'
    ))
    f.write(RateSAdd('120 ', '113.8 k', '114 k', 5.1, '132 ', '132 '))


    f.write(ER('14:53', 379585))
    # ====================================

    f.write(TAdd('Systems taken to local. All except TRG systems Calo L1 and Calo L2 put back.', 1))
    f.write(TAdd('New TRG keys tested. Maybe expect more TRG keys.', 1))
    f.write(TAdd('Proton beams cycling. Expect collisions later today.', 1))
    f.write(TAdd('All TRG systems functioned nominal. Rates were as expected.', 1))
    f.write(TTAdd('14:56', "Morning shift ended."))
