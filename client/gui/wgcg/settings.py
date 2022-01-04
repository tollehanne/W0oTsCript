# Embedded file name: scripts/client/gui/wgcg/settings.py
from shared_utils import CONST_CONTAINER

class WebRequestDataType(CONST_CONTAINER):
    LOGIN, LOGOUT, CLAN_INFO, CLAN_RATINGS, CLAN_GLOBAL_MAP_STATS, CLAN_ACCOUNTS, STRONGHOLD_INFO, STRONGHOLD_STATISTICS, ACCOUNT_APPLICATIONS_COUNT, CLAN_INVITATIONS_COUNT, CLAN_MEMBERS, CLAN_MEMBERS_RATING, SEARCH_CLANS, CLAN_PROVINCES, CLAN_APPLICATIONS, CLAN_INVITES, ACCOUNT_INVITES, ACCEPT_APPLICATION, ACCEPT_INVITE, CREATE_APPLICATIONS, CREATE_INVITES, DECLINE_APPLICATION, DECLINE_INVITE, DECLINE_INVITES, GET_RECOMMENDED_CLANS, GET_ACCOUNT_APPLICATIONS, CLANS_INFO, CLAN_FAVOURITE_ATTRS, PING, CLAN_GM_FRONTS, STRONGHOLD_LEAVE, STRONGHOLD_ASSIGN, STRONGHOLD_CHANGE_OPENED, STRONGHOLD_SET_VEHICLE, STRONGHOLD_SET_PLAYER_STATE, STRONGHOLD_SEND_INVITE, STRONGHOLD_KICK, STRONGHOLD_BATTLE_QUEUE, STRONGHOLD_GIVE_LEADERSHIP, STRONGHOLD_SET_RESERVE, STRONGHOLD_UPDATE, STRONGHOLD_TAKE_LEADERSHIP, STRONGHOLD_UNASSIGN, STRONGHOLD_UNSET_RESERVE, STRONGHOLD_JOIN_BATTLE, STRONGHOLD_SET_EQUIPMENT_COMMANDER, STRONGHOLD_MATCHMAKING_INFO, STRONGHOLD_SET_SLOT_VEHICLE_TYPE_FILTER, STRONGHOLD_SET_SLOT_VEHICLES_FILTER, STRONGHOLD_SLOT_VEHICLE_FILTERS_UPDATE, STRONGHOLD_STOP_PLAYERS_MATCHING, STRONGHOLD_LEAVE_MODE, RANKED_LEAGUE_POSITION, RANKED_YEAR_POSITION, HOF_USER_INFO, HOF_USER_EXCLUDE, HOF_USER_RESTORE, EVENT_BOARDS_GET_EVENTS_DATA, EVENT_BOARDS_GET_PLAYER_DATA, EVENT_BOARDS_JOIN_EVENT, EVENT_BOARDS_LEAVE_EVENT, EVENT_BOARDS_GET_MY_EVENT_TOP, EVENT_BOARDS_GET_MY_LEADERBOARD_POSITION, EVENT_BOARDS_GET_LEADERBOARD, EVENT_BOARDS_GET_HANGAR_FLAG, PROMO_GET_TEASER, PROMO_TEASER_SHOWN, PROMO_GET_UNREAD, PROMO_SEND_LOG, SPA_GET_ACCOUNT_ATTRIBUTE, PLATFORM_FETCH_PRODUCT_LIST, ADVENT_CALENDAR_FETCH_HERO_TANK_INFO, TOURNAMENT_LEAVE, TOURNAMENT_ASSIGN, TOURNAMENT_CHANGE_OPENED, TOURNAMENT_SET_VEHICLE, TOURNAMENT_SET_PLAYER_STATE, TOURNAMENT_SEND_INVITE, TOURNAMENT_KICK, TOURNAMENT_BATTLE_QUEUE, TOURNAMENT_GIVE_LEADERSHIP, TOURNAMENT_UPDATE, TOURNAMENT_TAKE_LEADERSHIP, TOURNAMENT_JOIN_BATTLE, TOURNAMENT_MATCHMAKING_INFO, TOURNAMENT_SET_SLOT_VEHICLE_TYPE_FILTER, TOURNAMENT_SET_SLOT_VEHICLES_FILTER, TOURNAMENT_SLOT_VEHICLE_FILTERS_UPDATE, TOURNAMENT_STOP_PLAYERS_MATCHING, TOURNAMENT_LEAVE_MODE, CRAFTMACHINE_MODULES_INFO, MAPBOX_PROGRESSION, MAPBOX_CREWBOOK, MAPBOX_SURVEY_COMPLETE, MAPBOX_SURVEY_URL, GIFT_SYSTEM_STATE, GIFT_SYSTEM_POST_GIFT = range(1, 98)


class ExternalBattleStorageName(CONST_CONTAINER):
    STRONGHOLD = 'wgsh'
    TOURNAMENT = 'tms'