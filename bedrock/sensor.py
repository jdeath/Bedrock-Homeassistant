from homeassistant.helpers.entity import Entity
from mcstatus import MinecraftBedrockServer
import mcstatus
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from datetime import timedelta
from homeassistant.util import Throttle

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=1)

from homeassistant.components.media_player import (
    MediaPlayerDevice, PLATFORM_SCHEMA)

CONF_URL = 'url'
CONF_PORT = 'port'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_URL): cv.string,
    vol.Required(CONF_PORT): cv.string,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    conf = discovery_info if discovery_info else config
    add_devices([ExampleSensor(conf[CONF_URL],conf[CONF_PORT])])


class ExampleSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self,url,port):
        """Initialize the sensor."""
        self._state = None
        self._url = url
        self._port = port;
        self.data = None
        self._attr = None
        self.change_detected = True
        self.update()
    @property
    def name(self):
        """Return the name of the sensor."""
        return 'bedrock'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return 'users'

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return 'mdi:minecraft'
    
    @Throttle(MIN_TIME_BETWEEN_UPDATES)    
    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = 0
        self._attr = {}
        bedrock_server = mcstatus.MinecraftBedrockServer.lookup(self._url)
        try:
            response = bedrock_server.status()
            self._attr["latency"] = response.latency
            self._attr["protocol"] = response.version.protocol
            self._attr["brand"] = response.version.brand
            self._attr["motd"] = response.motd
            self._attr["players_max"] = response.players_max
            self._attr["players_online"] = response.players_online
            self._attr["map"] = response.map
            self._attr["gamemode"] = response.gamemode
            self._state = response.players_online
        except:
            self._state = 0

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attr
