# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_shell_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NationChangeShellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties = 2, commands = 0):
        super(NationChangeShellModel, self).__init__(properties=properties, commands=commands)

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(NationChangeShellModel, self)._initialize()
        self._addResourceProperty('image', R.invalid())
        self._addNumberProperty('intCD', 0)