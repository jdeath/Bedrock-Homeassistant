"""Constants for the Minecraft Server integration."""
from collections import defaultdict
from typing import Dict, List, Literal, Set, Tuple

ATTR_PLAYERS_LIST = "players_list"

DEFAULT_HOST = "localhost:25565"
DEFAULT_NAME = "Minecraft Server"
DEFAULT_PORT = 25565

DOMAIN = "minecraft_server"

ICON_LATENCY_TIME = "mdi:signal"
ICON_PLAYERS_MAX = "mdi:account-multiple"
ICON_PLAYERS_ONLINE = "mdi:account-multiple"
ICON_PROTOCOL_VERSION = "mdi:numeric"
ICON_STATUS = "mdi:lan"
ICON_VERSION = "mdi:numeric"

KEY_SERVERS = "servers"

MANUFACTURER = "Mojang AB"

NAME_LATENCY_TIME = "Latency Time"
NAME_PLAYERS_MAX = "Players Max"
NAME_PLAYERS_ONLINE = "Players Online"
NAME_PROTOCOL_VERSION = "Protocol Version"
NAME_STATUS = "Status"
NAME_VERSION = "Version"

SCAN_INTERVAL = 60

SIGNAL_NAME_PREFIX = f"signal_{DOMAIN}"

SRV_RECORD_PREFIX = "_minecraft._tcp"

UNIT_PLAYERS_MAX = "players"
UNIT_PLAYERS_ONLINE = "players"
UNIT_PROTOCOL_VERSION = None
UNIT_VERSION = None

CONF_SERVER_TYPE: str = "server_type"
ConfServerType = Literal["Java", "Bedrock"]
CONF_SERVER_TYPE_JAVA: ConfServerType = "Java"
CONF_SERVER_TYPE_BEDROCK: ConfServerType = "Bedrock"
CONF_SERVER_TYPE_ALL: List[str] = [
    CONF_SERVER_TYPE_JAVA,
    CONF_SERVER_TYPE_BEDROCK,
]