import logging
import requests
from homeassistant.components.cover import CoverEntity
from homeassistant.const import STATE_CLOSED, STATE_OPEN
from .const import DOMAIN, CONF_IP_ADDRESS, CONF_API_KEY

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip = config_entry.data[CONF_IP_ADDRESS]
    api_key = config_entry.data[CONF_API_KEY]
    async_add_entities([CenturionGarageDoor(ip, api_key)], update_before_add=True)

class CenturionGarageDoor(CoverEntity):
    def __init__(self, ip, api_key):
        self._ip = ip
        self._api_key = api_key
        self._state = STATE_CLOSED
        self._attr_unique_id = f"centurion_garage_{ip.replace('.', '_')}"

    def _base_url(self):
        return f"http://{self._ip}/api?key={self._api_key}"

    def update(self):
        try:
            response = requests.get(f"{self._base_url()}&status=json", timeout=5)
            data = response.json()
            self._state = STATE_OPEN if data["door"] == "open" else STATE_CLOSED
        except Exception as e:
            _LOGGER.error(f"Error updating Centurion door status: {e}")

    @property
    def name(self):
        return "Centurion Garage Door"

    @property
    def is_closed(self):
        return self._state == STATE_CLOSED

    def open_cover(self, **kwargs):
        requests.get(f"{self._base_url()}&door=open")
        self._state = STATE_OPEN
        self.schedule_update_ha_state()

    def close_cover(self, **kwargs):
        requests.get(f"{self._base_url()}&door=close")
        self._state = STATE_CLOSED
        self.schedule_update_ha_state()

    def stop_cover(self, **kwargs):
        requests.get(f"{self._base_url()}&door=stop")
