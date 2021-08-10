# Embedded file name: scripts/client/gui/prb_control/entities/training/pre_queue/vehicles_watcher.py
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.requesters import REQ_CRITERIA
from skeletons.gui.shared import IItemsCache
from helpers import dependency

class TrainingVehiclesWatcher(BaseVehiclesWatcher):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getUnsuitableVehicles(self, onClear = False):
        unsuitableVehicles = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.EPIC_BATTLE ^ REQ_CRITERIA.VEHICLE.EVENT_BATTLE).itervalues()
        return unsuitableVehicles