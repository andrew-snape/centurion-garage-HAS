import requests
from datetime import timedelta
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import DeviceInfo
from .const import CONF_IP_ADDRESS, CONF_API_KEY, DOMAIN

SCAN_INTERVAL = timedelta(seconds=30)

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip = config_entry.data[CONF_IP_ADDRESS]
    api_key = config_entry.data[CONF_API_KEY]
    async_add_entities([
        CenturionLampSwitch(ip, api_key),
        CenturionVacationSwitch(ip, api_key)
    ])

class CenturionBaseSwitch(SwitchEntity):
    def __init__(self, ip, api_key):
        self._ip = ip
        self._api_key = api_key
        self._is_on = False

    def _base_url(self):
        return f"http://{self._ip}/api?key={self._api_key}"

    @property
    def device_info(self):
        return DeviceInfo(
            identifiers = {(DOMAIN, self._ip)},
            name = "Centurion Garage Door",
            manufacturer = "Centurion",
            model = "Smart Garage"
        )

class CenturionLampSwitch(CenturionBaseSwitch):
    def __init__(self, ip, api_key):
        super().__init__(ip, api_key)
        self._attr_unique_id = f"centurion_lamp_{ip.replace('.', '_')}"
        self._attr_name = "Centurion Garage Lamp"

    @property
    def is_on(self):
        return self._is_on

    @property
    def icon(self):
        return "mdi:lightbulb"

    def turn_on(self, **kwargs):
        requests.get(f"{self._base_url()}&lamp=on")
        self._is_on = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        requests.get(f"{self._base_url()}&lamp=off")
        self._is_on = False
        self.schedule_update_ha_state()

    def update(self):
        try:
            r = requests.get(f"{self._base_url()}&status=json", timeout=5)
            data = r.json()
            self._is_on = str(data.get("lamp", "off")).lower() == "on"
        except Exception:
            self._is_on = False

class CenturionVacationSwitch(CenturionBaseSwitch):
    def __init__(self, ip, api_key):
        super().__init__(ip, api_key)
        self._attr_unique_id = f"centurion_vacation_{ip.replace('.', '_')}"
        self._attr_name = "Centurion Vacation Mode"

    @property
    def is_on(self):
        return self._is_on

    @property
    def icon(self):
        return "mdi:beach"

    def turn_on(self, **kwargs):
        requests.get(f"{self._base_url()}&vacation=on")
        self._is_on = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        requests.get(f"{self._base_url()}&vacation=off")
        self._is_on = False
        self.schedule_update_ha_state()

    def update(self):
        try:
            r = requests.get(f"{self._base_url()}&status=json", timeout=5)
            data = r.json()
            self._is_on = str(data.get("vacation", "off")).lower() == "on"
        except Exception:
            self._is_on = False
