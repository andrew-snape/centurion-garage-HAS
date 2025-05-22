import requests
from homeassistant.components.switch import SwitchEntity
from .const import CONF_IP_ADDRESS, CONF_API_KEY

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip = config_entry.data[CONF_IP_ADDRESS]
    api_key = config_entry.data[CONF_API_KEY]
    async_add_entities([
        CenturionLampSwitch(ip, api_key),
        CenturionVacationSwitch(ip, api_key)
    ])

class CenturionLampSwitch(SwitchEntity):
    def __init__(self, ip, api_key):
        self._ip = ip
        self._api_key = api_key
        self._is_on = False
        self._attr_unique_id = f"centurion_lamp_{ip.replace('.', '_')}"

    @property
    def name(self):
        return "Centurion Garage Lamp"

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self, **kwargs):
        requests.get(f"http://{self._ip}/api?key={self._api_key}&lamp=on")
        self._is_on = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        requests.get(f"http://{self._ip}/api?key={self._api_key}&lamp=off")
        self._is_on = False
        self.schedule_update_ha_state()

class CenturionVacationSwitch(SwitchEntity):
    def __init__(self, ip, api_key):
        self._ip = ip
        self._api_key = api_key
        self._is_on = False
        self._attr_unique_id = f"centurion_vacation_{ip.replace('.', '_')}"

    @property
    def name(self):
        return "Centurion Vacation Mode"

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self, **kwargs):
        requests.get(f"http://{self._ip}/api?key={self._api_key}&vacation=on")
        self._is_on = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        requests.get(f"http://{self._ip}/api?key={self._api_key}&vacation=off")
        self._is_on = False
        self.schedule_update_ha_state()
