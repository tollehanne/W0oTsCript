# Embedded file name: scripts/client/gui/shared/utils/requesters/anonymizer_requester.py
import typing
import BigWorld
from adisp import async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IAnonymizerRequester

class AnonymizerRequester(AbstractSyncDataRequester, IAnonymizerRequester):

    @property
    def isPlayerAnonymized(self):
        return bool(self.getCacheValue('enabled', 0))

    @property
    def contactsFeedback(self):
        return self.getCacheValue('contactsFeedback', list())

    @async
    def _requestCache(self, callback):
        BigWorld.player().anonymizer.getCache(lambda resID, value: self._response(resID, value, callback))