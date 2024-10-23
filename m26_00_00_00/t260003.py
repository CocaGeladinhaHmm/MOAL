# -*- coding: utf-8 -*-
def t260003_0():
    """State 0,1"""
    t260003_x1(flag1=6000, flag2=6001, actionbutton1=6100, actionbutton2=6101, flag3=260, flag4=3, action1=10010715)
    Quit()

def t260003_x0():
    """State 0,1"""
    assert t260003_x7(z1=99999, z2=99999, z3=99999, z4=99999)
    """State 2"""
    return 0

def t260003_x1(flag1=6000, flag2=6001, actionbutton1=6100, actionbutton2=6101, flag3=260, flag4=3, action1=10010715):
    """State 0"""
    while True:
        """State 2"""
        DebugEvent('地上子ワープ椅子_非マルチ中')
        call = t260003_x3(actionbutton1=actionbutton1, actionbutton2=actionbutton2, flag3=flag3, flag4=flag4,
                          action1=action1)
        if IsMultiplayerInProgress() == 1:
            """State 1"""
            DebugEvent('地上子ワープ椅子_マルチ中')
            call = t260003_x2(actionbutton1=actionbutton1, flag3=flag3, flag4=flag4, action1=action1)
            if not IsMultiplayerInProgress():
                continue
            elif not GetEventStatus(flag1) or GetEventStatus(flag2) == 1:
                pass
        elif not GetEventStatus(flag1) or GetEventStatus(flag2) == 1:
            pass
        """State 3"""
        DebugEvent('地上子ワープ椅子_アクセス不可')
        call = t260003_x5()
        assert GetEventStatus(flag1) == 1 and not GetEventStatus(flag2)
    """Unused"""
    """State 4"""
    return 0

def t260003_x2(actionbutton1=6100, flag3=260, flag4=3, action1=10010715):
    """State 0,3"""
    ForceCloseMenu()
    while True:
        """State 2"""
        if GetEventStatus(10007810 + flag3 * 10000 + flag4 * 20) == 1:
            pass
        elif (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and
              not IsPlayerDead() and not IsCharacterDisabled() and CheckActionButtonArea(actionbutton1)):
            """State 4"""
            ClearPlayerDamageInfo()
            SetTalkTime(0.33)
            """State 5"""
            call = t260003_x8(flag3=flag3, flag4=flag4, action1=action1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 3 or HasPlayerBeenAttacked() == 1:
                continue
        """State 1"""
        assert not GetEventStatus(10007810 + flag3 * 10000 + flag4 * 20)
    """Unused"""
    """State 6"""
    return 0

def t260003_x3(actionbutton1=6100, actionbutton2=6101, flag3=260, flag4=3, action1=10010715):
    """State 0"""
    while True:
        """State 2"""
        Label('L0')
        DebugEvent('稼動状態_非マルチ中')
        if not GetEventStatus(10007810 + flag3 * 10000 + flag4 * 20):
            break
        elif (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and
              not IsPlayerDead() and not IsCharacterDisabled() and CheckActionButtonArea(actionbutton2)):
            """State 3"""
            ClearPlayerDamageInfo()
            SetTalkTime(0.33)
            """State 6"""
            call = t260003_x4(flag3=flag3, flag4=flag4, action1=action1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 3 or HasPlayerBeenAttacked() == 1:
                """State 5"""
                assert t260003_x0()
    while True:
        """State 1"""
        DebugEvent('非稼動状態_非マルチ中')
        if GetEventStatus(10007810 + flag3 * 10000 + flag4 * 20) == 1:
            Goto('L0')
        elif (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and
              not IsPlayerDead() and not IsCharacterDisabled() and CheckActionButtonArea(actionbutton1)):
            """State 4"""
            ClearPlayerDamageInfo()
            SetTalkTime(0.33)
            """State 7"""
            call = t260003_x8(flag3=flag3, flag4=flag4, action1=action1)
            if call.Done() and GetEventStatus(10007810 + flag3 * 10000 + flag4 * 20) == 1:
                Goto('L0')
            elif GetDistanceToPlayer() > 3 or HasPlayerBeenAttacked() == 1:
                """State 8"""
                assert t260003_x0()
    """Unused"""
    """State 9"""
    return 0

def t260003_x4(flag3=260, flag4=3, action1=10010715):
    while True:
        ClearTalkListData()
        AddTalkListData(1, 70011001, -1)
        AddTalkListData(2, 15000100, -1)
        AddTalkListData(3, 15000110, -1)
        AddTalkListData(9, 15000120, -1)
        AddTalkListData(10, 15000111, -1)
        AddTalkListData(11, 10011050, -1)
        AddTalkListData(4, 10011080, -1)
        AddTalkListData(5, 15000140, -1)
        AddTalkListData(6, 15000140, -1)
        AddTalkListData(7, 15000141, -1)
        AddTalkListData(8, 10011020, -1)
        AddTalkListData(99, 15000005, -1)
        ShowShopMessage(0, 0, 0)
        if not GetTalkListEntryResult() or GetTalkListEntryResult() == 99 or not IsTalkExclusiveMenuOpen():
            return 0
        elif GetDistanceToPlayer() > 3 or HasPlayerBeenAttacked() == 1:
            assert t260003_x0()
            return 0
        elif GetTalkListEntryResult() == 1:
            if not GetEventStatus(flag3 * 10 + 70000000 + flag4 * 1):
                OpenGenericDialog(2, 10010713, 3, 4, 2)
                def WhilePaused():
                    SetTalkTime(0.33)
                if GetGenericDialogButtonResult() == 1:
                    DebugEvent('OK')
                    assert t260003_x6(flag3=flag3, flag4=flag4, z5=0)
                elif not IsGenericDialogOpen():
                    DebugEvent('CANCEL')
            else:
                OpenGenericDialog(7, action1, 1, 0, 1)
                def WhilePaused():
                    SetTalkTime(0.33)
                assert not IsGenericDialogOpen()
            return 0
        elif GetTalkListEntryResult() == 2:
            assert t260003_x102()
        elif GetTalkListEntryResult() == 3:
            assert t260003_x103()
        elif GetTalkListEntryResult() == 4:
            assert t260003_x104()
        elif GetTalkListEntryResult() == 5:
            assert t260003_x105()
        elif GetTalkListEntryResult() == 6:
            assert t260003_x106()
        elif GetTalkListEntryResult() == 7:
            assert t260003_x107()
        elif GetTalkListEntryResult() == 8:
            assert t260003_x108()
        elif GetTalkListEntryResult() == 9:
            assert t260003_x109()
        elif GetTalkListEntryResult() == 10:
            assert t260003_x110()
        elif GetTalkListEntryResult() == 11:
            assert t260003_x111()


def t260003_x5():
    """State 0,1"""
    DebugEvent('待機_アクセス不可')
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t260003_x6(flag3=260, flag4=3, z5=0):
    """State 0,1"""
    SetEventState(flag3 * 10000 + 70000100 + flag4 * 1, 1)
    """State 2"""
    return 0

def t260003_x7(z1=99999, z2=99999, z3=99999, z4=99999):
    """State 0,1"""
    DebugEvent('会話判定')
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    DebugEvent('汎用ダイアログ判定')
    if IsGenericDialogOpen() == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    DebugEvent('メニュー判定')
    if (CheckSpecificPersonMenuIsOpen(z1, 0) == 1 or CheckSpecificPersonMenuIsOpen(z2, 0) == 1 or CheckSpecificPersonMenuIsOpen(z3,
        0) == 1 or CheckSpecificPersonMenuIsOpen(z4, 0) == 1):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t260003_x8(flag3=260, flag4=3, action1=10010715):
    """State 0,2"""
    if not GetEventStatus(flag3 * 10 + 70000000 + flag4 * 1):
        """State 3"""
        SetEventState(flag3 * 10000 + 70000200 + flag4 * 1, 1)
        def WhilePaused():
            c1_73(1)
        """State 4"""
        if GetEventStatus(6715) == 1:
            pass
        else:
            """State 6"""
            DebugEvent('ダイアログ表示許可待ち')
            assert GetEventStatus(70000030) == 1
            """State 5"""
            OpenGenericDialog(1, 10011240, 1, 0, 1)
            def WhilePaused():
                SetTalkTime(0.33)
            assert not IsGenericDialogOpen()
    else:
        """State 1"""
        OpenGenericDialog(7, action1, 1, 0, 1)
        def WhilePaused():
            SetTalkTime(0.33)
        assert not IsGenericDialogOpen()
    """State 7"""
    return 0

def t260003_x102():
    assert not IsGenericDialogOpen()
    OpenSoul()
    assert not CheckSpecificPersonMenuIsOpen(23, 0)
    return 0

def t260003_x103():
    assert not IsGenericDialogOpen()
    OpenEquipmentChangeOfPurposeShop()
    assert not CheckSpecificPersonMenuIsOpen(13, 0)
    return 0

def t260003_x104():
    assert not IsGenericDialogOpen()
    OpenCaryllRuneEquipMenu()
    assert not CheckSpecificPersonMenuIsOpen(1001, 0)
    return 0

def t260003_x105():
    DebugEvent('購入')
    OpenCaryllRuneEquipMenu()
    OpenInsightShop(200000, 200099)
    assert not CheckSpecificPersonMenuIsOpen(370, 0)
    return 0

def t260003_x106():
    DebugEvent('購入')
    if GetEventStatus(6603) == 1:
        OpenRegularShop(140000, 149999)
        def WhilePaused():
            SetTalkTime(0.33)
        assert not CheckSpecificPersonMenuIsOpen(11, 0)
    elif GetEventStatus(9802) == 1:
        OpenRegularShop(130000, 139999)
        def WhilePaused():
            SetTalkTime(0.33)
        assert not CheckSpecificPersonMenuIsOpen(11, 0)
    elif GetEventStatus(9801) == 1:
        OpenRegularShop(120000, 129999)
        def WhilePaused():
            SetTalkTime(0.33)
        assert not CheckSpecificPersonMenuIsOpen(11, 0)
    elif GetEventStatus(9800) == 1:
        OpenRegularShop(110000, 119999)
        def WhilePaused():
            SetTalkTime(0.33)
        assert not CheckSpecificPersonMenuIsOpen(11, 0)
    else:
        """State 1"""
        OpenRegularShop(100000, 109999)
        def WhilePaused():
            SetTalkTime(0.33)
        assert not CheckSpecificPersonMenuIsOpen(11, 0)
    return 0

def t260003_x107():
    DebugEvent('売却')
    OpenSellShop(-1, -1)
    def WhilePaused():
        SetTalkTime(0.33)
    assert not CheckSpecificPersonMenuIsOpen(64, 0)
    return 0

def t260003_x108():
    assert not IsGenericDialogOpen()
    OpenRepository()
    assert not CheckSpecificPersonMenuIsOpen(200, 0)
    return 0

def t260003_x109():
    assert not IsGenericDialogOpen()
    OpenRepairShop()
    assert not CheckSpecificPersonMenuIsOpen(12, 0)
    return 0

def t260003_x110():
    assert not IsGenericDialogOpen()
    OpenBloodGemEquipMenu()
    assert not CheckSpecificPersonMenuIsOpen(1000, 0)
    return 0

def t260003_x111():
    assert not IsGenericDialogOpen()
    OpenArcaneHazeExtractorMenu()
    assert not CheckSpecificPersonMenuIsOpen(380, 0)
    return 0
