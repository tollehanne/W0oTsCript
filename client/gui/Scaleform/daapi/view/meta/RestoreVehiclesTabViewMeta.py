# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RestoreVehiclesTabViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.vehicle_view import VehicleView

class RestoreVehiclesTabViewMeta(VehicleView):

    def restoreItem(self, itemId):
        self._printOverrideError('restoreItem')