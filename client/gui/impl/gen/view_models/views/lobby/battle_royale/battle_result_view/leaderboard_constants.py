# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_royale/battle_result_view/leaderboard_constants.py
from frameworks.wulf import ViewModel

class LeaderboardConstants(ViewModel):
    __slots__ = ()
    ROW_TYPE_BR_PLAYER = 'rowBrPlayer'
    ROW_TYPE_BR_ENEMY = 'rowBrEnemy'

    def __init__(self, properties = 0, commands = 0):
        super(LeaderboardConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LeaderboardConstants, self)._initialize()