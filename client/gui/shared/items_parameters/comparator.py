# Embedded file name: scripts/client/gui/shared/items_parameters/comparator.py
import collections
import sys
from constants import BonusTypes
from gui.shared.items_parameters import params_cache
from gui.shared.utils import WHEELED_SWITCH_ON_TIME, WHEELED_SWITCH_OFF_TIME, DUAL_GUN_CHARGE_TIME, TURBOSHAFT_INVISIBILITY_STILL_FACTOR, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, CHASSIS_REPAIR_TIME
BACKWARD_QUALITY_PARAMS = frozenset(['aimingTime',
 'shotDispersionAngle',
 'weight',
 'dispertionRadius',
 'fireStartingChance',
 'reloadTimeSecs',
 'autoReloadTime',
 'shellReloadingTime',
 'clipFireRate',
 'reloadMagazineTime',
 'weight',
 'switchOnTime',
 'switchOffTime',
 WHEELED_SWITCH_ON_TIME,
 WHEELED_SWITCH_OFF_TIME,
 DUAL_GUN_CHARGE_TIME,
 'vehicleOwnSpottingTime',
 'vehicleGunShotDispersion',
 'crewStunDuration',
 'vehicleReloadTimeAfterShellChange',
 'crewRepeatedStunDuration',
 'vehicleChassisFallDamage',
 'vehPenaltyForDamageEngineAndCombat',
 'demaskFoliageFactor',
 'demaskMovingFactor',
 'vehicleRamOrExplosionDamageResistance',
 'vehicleFireChance',
 CHASSIS_REPAIR_TIME,
 'vehicleGunShotFullDispersion',
 'vehicleGunShotDispersionAfterShot',
 'vehicleGunShotDispersionChassisMovement',
 'vehicleGunShotDispersionChassisRotation',
 'vehicleGunShotDispersionTurretRotation',
 'vehicleGunShotDispersionWhileGunDamaged',
 'vehicleRamDamageResistance',
 'vehicleGunReloadTime'])
NEGATIVE_PARAMS = ['switchOnTime', 'switchOffTime']
_CUSTOM_QUALITY_PARAMS = {'vehicleWeight': (True, False),
 'clipFireRate': (True, True, False),
 'pitchLimits': (True, False)}

class PARAM_STATE(object):
    WORSE = 'worse'
    NORMAL = 'normal'
    BETTER = 'better'
    NOT_APPLICABLE = 'N/A'


DEFAULT_AVG_VALUE = (sys.maxint, -1)

def getParamExtendedData(paramName, value, otherValue, penalties = None, customQualityParams = None):
    possibleBonuses, bonuses, inactive, penalties = penalties if penalties is not None else ([],
     [],
     [],
     [])
    if paramName not in NEGATIVE_PARAMS:
        if otherValue is None or otherValue == DEFAULT_AVG_VALUE:
            otherValue = value
    return _ParameterInfo(paramName, value, rateParameterState(paramName, value, otherValue, customQualityParams=customQualityParams), possibleBonuses, inactive, bonuses, penalties)


class ItemsComparator(object):

    def __init__(self, currentParams, otherParams):
        super(ItemsComparator, self).__init__()
        self._currentParams = currentParams
        self._otherParams = otherParams

    def getAllDifferentParams(self):
        result = []
        for paramName in self._currentParams.keys():
            data = self.getExtendedData(paramName)
            if data.state[0] != PARAM_STATE.NORMAL:
                result.append(data)

        return result

    def getExtendedData(self, paramName):
        return getParamExtendedData(paramName, self._currentParams.get(paramName), self._otherParams.get(paramName), self._getPenaltiesAndBonuses(paramName))

    def _getPenaltiesAndBonuses(self, _):
        return ([],
         [],
         {},
         [])


class VehiclesComparator(ItemsComparator):

    def __init__(self, currentVehicleParams, otherVehicleParams, suitableArtefacts = None, bonuses = None, penalties = None):
        super(VehiclesComparator, self).__init__(currentVehicleParams, otherVehicleParams)
        self.__suitableArtefacts = suitableArtefacts or set()
        self.__bonuses = bonuses or set()
        self.__penalties = penalties or dict()

    def hasBonusOfType(self, bnsType):
        return any((i == bnsType for _, i in self.__bonuses))

    def _getPenaltiesAndBonuses(self, paramName):
        penalties = self.__penalties.get(paramName, [])
        allPossibleParamBonuses = self.__getPossibleParamBonuses(paramName)
        currentParamBonuses, inactive = self.__getCurrentParamBonuses(paramName, allPossibleParamBonuses)
        possibleBonuses = allPossibleParamBonuses - currentParamBonuses
        return (possibleBonuses,
         currentParamBonuses,
         inactive,
         penalties)

    def __getPossibleParamBonuses(self, paramName):
        paramBonuses = set(params_cache.g_paramsCache.getBonuses().get(paramName, []))
        allPossibleParamBonuses = set()
        for bonusName, bonusGroup in paramBonuses:
            if (bonusName, bonusGroup) in self.__suitableArtefacts or bonusGroup in BonusTypes.POSSIBLE:
                allPossibleParamBonuses.add((bonusName, bonusGroup))

        return allPossibleParamBonuses

    def __getCurrentParamBonuses(self, paramName, possibleBonuses):
        if paramName in CONDITIONAL_BONUSES:
            return self.__getConditionalBonuses(paramName, possibleBonuses)
        return (possibleBonuses.intersection(self.__bonuses), {})

    def __getConditionalBonuses(self, paramName, possibleBonuses):
        currentBonuses, affectedBonuses = set(), {}
        condition, affected = CONDITIONAL_BONUSES[paramName]
        bonuses = possibleBonuses.intersection(self.__bonuses)
        for bonus in bonuses:
            isAffected = bonus in affected
            if not isAffected or isAffected and condition in bonuses:
                currentBonuses.add(bonus)
            elif isAffected:
                affectedBonuses[bonus] = condition

        return (currentBonuses, affectedBonuses)


class _ParameterInfo(collections.namedtuple('_ParameterInfo', ('name', 'value', 'state', 'possibleBonuses', 'inactiveBonuses', 'bonuses', 'penalties'))):

    def getParamDiff(self):
        if isinstance(self.value, (tuple, list)):
            diff = [ d for _, d in self.state ]
            if any(diff):
                return diff
        else:
            _, diff = self.state
            if diff is not None:
                return diff
        return


CONDITIONAL_BONUSES = {('invisibilityMovingFactor',
 'invisibilityStillFactor',
 TURBOSHAFT_INVISIBILITY_MOVING_FACTOR,
 TURBOSHAFT_INVISIBILITY_STILL_FACTOR): (('camouflage', BonusTypes.SKILL), [('brotherhood', BonusTypes.SKILL),
                                                                                                                                            ('chocolate', BonusTypes.EQUIPMENT),
                                                                                                                                            ('cocacola', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration', BonusTypes.EQUIPMENT),
                                                                                                                                            ('hotCoffee', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_china', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_uk', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_japan', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_czech', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_sweden', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_poland', BonusTypes.EQUIPMENT),
                                                                                                                                            ('ration_italy', BonusTypes.EQUIPMENT),
                                                                                                                                            ('improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                            ('improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                            ('improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                            ('deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE)]),
 (CHASSIS_REPAIR_TIME,): (('repair', BonusTypes.SKILL), [('brotherhood', BonusTypes.SKILL),
                           ('chocolate', BonusTypes.EQUIPMENT),
                           ('cocacola', BonusTypes.EQUIPMENT),
                           ('ration', BonusTypes.EQUIPMENT),
                           ('hotCoffee', BonusTypes.EQUIPMENT),
                           ('ration_china', BonusTypes.EQUIPMENT),
                           ('ration_uk', BonusTypes.EQUIPMENT),
                           ('ration_japan', BonusTypes.EQUIPMENT),
                           ('ration_czech', BonusTypes.EQUIPMENT),
                           ('ration_sweden', BonusTypes.EQUIPMENT),
                           ('ration_poland', BonusTypes.EQUIPMENT),
                           ('ration_italy', BonusTypes.EQUIPMENT),
                           ('improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                           ('improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                           ('improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                           ('deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                           ('trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                           ('trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE)])}
CONDITIONAL_BONUSES = {k:v for keys, v in CONDITIONAL_BONUSES.items() for k in keys}

def _getComparableValue(currentValue, comparableList, idx):
    if len(comparableList) > idx:
        return comparableList[idx]
    return currentValue


def _getParamStateInfo(paramName, val1, val2, customReverted = False):
    if val1 is None or val2 is None:
        hasNoParam = True
        diff = 0
    else:
        hasNoParam = False
        if isinstance(val1, float) and isinstance(val2, float):
            diff = val1 - val2
            diff = round(diff, 2)
        else:
            if isinstance(val1, float):
                val1 = round(val1, 2)
            if isinstance(val2, float):
                val2 = round(val2, 2)
            diff = val1 - val2
    if paramName in NEGATIVE_PARAMS and hasNoParam:
        if val1 is None and val2 is None:
            return (PARAM_STATE.NORMAL, diff)
        if val1 is None:
            return (PARAM_STATE.BETTER, diff)
        return (PARAM_STATE.WORSE, diff)
    elif diff == 0:
        return (PARAM_STATE.NORMAL, diff)
    isInverted = paramName in BACKWARD_QUALITY_PARAMS or customReverted
    if isInverted and diff > 0 or not isInverted and diff < 0:
        return (PARAM_STATE.WORSE, diff)
    else:
        return (PARAM_STATE.BETTER, diff)


def rateParameterState(paramName, val1, val2, customQualityParams = None):
    if isinstance(val1, (tuple, list)):
        if customQualityParams is None:
            customQualityParams = _CUSTOM_QUALITY_PARAMS.get(paramName)
        customQualityLen = len(customQualityParams) if customQualityParams else 0
        result = []
        val2Len = len(val2)
        for i, val in enumerate(val1):
            if val2Len == 0:
                result.append((PARAM_STATE.NORMAL, None))
                continue
            if val2Len > i:
                val2ToCompare = val2[i]
            else:
                result.append((PARAM_STATE.NOT_APPLICABLE, None))
                continue
            if customQualityParams is not None:
                customQuality = customQualityParams[min(i, customQualityLen - 1)]
            else:
                customQuality = None
            result.append(rateParameterState(paramName, val, val2ToCompare, customQuality))

        return tuple(result)
    else:
        return _getParamStateInfo(paramName, val1, val2, customQualityParams)