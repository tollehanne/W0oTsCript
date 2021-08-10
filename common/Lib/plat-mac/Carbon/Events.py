# Embedded file name: scripts/common/Lib/plat-mac/Carbon/Events.py
nullEvent = 0
mouseDown = 1
mouseUp = 2
keyDown = 3
keyUp = 4
autoKey = 5
updateEvt = 6
diskEvt = 7
activateEvt = 8
osEvt = 15
kHighLevelEvent = 23
mDownMask = 1 << mouseDown
mUpMask = 1 << mouseUp
keyDownMask = 1 << keyDown
keyUpMask = 1 << keyUp
autoKeyMask = 1 << autoKey
updateMask = 1 << updateEvt
diskMask = 1 << diskEvt
activMask = 1 << activateEvt
highLevelEventMask = 1024
osMask = 1 << osEvt
everyEvent = 65535
charCodeMask = 255
keyCodeMask = 65280
adbAddrMask = 16711680
mouseMovedMessage = 250
suspendResumeMessage = 1
resumeFlag = 1
convertClipboardFlag = 2
activeFlagBit = 0
btnStateBit = 7
cmdKeyBit = 8
shiftKeyBit = 9
alphaLockBit = 10
optionKeyBit = 11
controlKeyBit = 12
rightShiftKeyBit = 13
rightOptionKeyBit = 14
rightControlKeyBit = 15
activeFlag = 1 << activeFlagBit
btnState = 1 << btnStateBit
cmdKey = 1 << cmdKeyBit
shiftKey = 1 << shiftKeyBit
alphaLock = 1 << alphaLockBit
optionKey = 1 << optionKeyBit
controlKey = 1 << controlKeyBit
rightShiftKey = 1 << rightShiftKeyBit
rightOptionKey = 1 << rightOptionKeyBit
rightControlKey = 1 << rightControlKeyBit
kNullCharCode = 0
kHomeCharCode = 1
kEnterCharCode = 3
kEndCharCode = 4
kHelpCharCode = 5
kBellCharCode = 7
kBackspaceCharCode = 8
kTabCharCode = 9
kLineFeedCharCode = 10
kVerticalTabCharCode = 11
kPageUpCharCode = 11
kFormFeedCharCode = 12
kPageDownCharCode = 12
kReturnCharCode = 13
kFunctionKeyCharCode = 16
kCommandCharCode = 17
kCheckCharCode = 18
kDiamondCharCode = 19
kAppleLogoCharCode = 20
kEscapeCharCode = 27
kClearCharCode = 27
kLeftArrowCharCode = 28
kRightArrowCharCode = 29
kUpArrowCharCode = 30
kDownArrowCharCode = 31
kSpaceCharCode = 32
kDeleteCharCode = 127
kBulletCharCode = 165
kNonBreakingSpaceCharCode = 202
kShiftUnicode = 8679
kControlUnicode = 8963
kOptionUnicode = 8997
kCommandUnicode = 8984
kPencilUnicode = 9998
kCheckUnicode = 10003
kDiamondUnicode = 9670
kBulletUnicode = 8226
kAppleLogoUnicode = 63743
networkEvt = 10
driverEvt = 11
app1Evt = 12
app2Evt = 13
app3Evt = 14
app4Evt = 15
networkMask = 1024
driverMask = 2048
app1Mask = 4096
app2Mask = 8192
app3Mask = 16384
app4Mask = 32768