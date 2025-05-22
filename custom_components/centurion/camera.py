from homeassistant.components.camera import Camera
from .const import CONF_IP_ADDRESS

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip = config_entry.data[CONF_IP_ADDRESS]
    async_add_entities([CenturionCamera(ip)], update_before_add=True)

class CenturionCamera(Camera):
    def __init__(self, ip):
        super().__init__()
        self._ip = ip
        self._attr_unique_id = f"centurion_camera_{ip.replace('.', '_')}"
        self._attr_name = "Centurion Garage Camera"

    async def async_camera_image(self):
        return None

    @property
    def stream_source(self):
        return f"http://{self._ip}:88/"
