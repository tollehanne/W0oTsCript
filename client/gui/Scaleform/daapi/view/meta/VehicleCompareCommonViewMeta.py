# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareCommonViewMeta.py
from gui.Scaleform.framework.entities.View import View

class VehicleCompareCommonViewMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')