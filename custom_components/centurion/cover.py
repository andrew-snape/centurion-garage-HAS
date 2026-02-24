import logging
import requests
from homeassistant.components.cover import CoverEntity
from homeassistant.const import STATE_CLOSED, STATE_OPEN, STATE_OPENING, STATE_CLOSING
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

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._ip)},
            "name": "Centurion Garage Door",
            "manufacturer": "Centurion",
            "model": "Smart Garage"
        }

    @property
    def device_class(self):
        return "garage"

    @property
    def supported_features(self):
        # OPEN, CLOSE, STOP
        return 7

    def update(self):
        try:
            url = f"{self._base_url()}&status=json"
            _LOGGER.debug(f"Fetching door status from: {url}")
            response = requests.get(url, timeout=5)
            data = response.json()
            door_state = str(data.get("door", "")).lower()
            _LOGGER.debug(f"Centurion returned door state: {door_state}")

            if "opening" in door_state:
                self._state = STATE_OPENING
            elif "closing" in door_state:
                self._state = STATE_CLOSING
            elif "open" in door_state:
                self._state = STATE_OPEN
            elif "close" in door_state:
                self._state = STATE_CLOSED
            elif "stopped" in door_state or "error" in door_state:
                self._state = None
                _LOGGER.warning(f"Door in stopped/error state: {door_state}")
            else:
                _LOGGER.warning(f"Unexpected door state: {door_state}")
                self._state = None

        except Exception as e:
            _LOGGER.error(f"Error updating Centurion door status: {e}")

    @property
    def name(self):
        return "Centurion Garage Door"

    @property
    def is_closed(self):
        return self._state == STATE_CLOSED

    @property
    def state(self):
        return self._state

    def open_cover(self, **kwargs):
        try:
            requests.get(f"{self._base_url()}&door=open")
            self._state = STATE_OPEN
            self.schedule_update_ha_state()
        except Exception as e:
            _LOGGER.error(f"Error sending open command: {e}")

    def close_cover(self, **kwargs):
        try:
            requests.get(f"{self._base_url()}&door=close")
            self._state = STATE_CLOSED
            self.schedule_update_ha_state()
        except Exception as e:
            _LOGGER.error(f"Error sending close command: {e}")

    def stop_cover(self, **kwargs):
        try:
            requests.get(f"{self._base_url()}&door=stop")
        except Exception as e:
            _LOGGER.error(f"Error sending stop command: {e}")
