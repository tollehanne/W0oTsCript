# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RentVehiclesTabViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.category_view import InventoryCategoryView

class RentVehiclesTabViewMeta(InventoryCategoryView):

    def removeItem(self, itemId):
        self._printOverrideError('removeItem')