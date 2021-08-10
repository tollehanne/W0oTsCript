# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_setup_selector.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_setup_selector import AmmunitionSetupSelector

class PrebattleAmmunitionSetupSelector(AmmunitionSetupSelector):
    __slots__ = ()

    def __init__(self, properties = 3, commands = 0):
        super(PrebattleAmmunitionSetupSelector, self).__init__(properties=properties, commands=commands)

    def getHotKeys(self):
        return self._getArray(2)

    def setHotKeys(self, value):
        self._setArray(2, value)

    def _initialize(self):
        super(PrebattleAmmunitionSetupSelector, self)._initialize()
        self._addArrayProperty('hotKeys', Array())