from .const import DOMAIN
import asyncio

PLATFORMS = ["cover", "camera", "switch"]

async def async_setup_entry(hass, config_entry):
    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(config_entry, platform)
        )
    return True

async def async_unload_entry(hass, config_entry):
    return all(
        await asyncio.gather(
            *[hass.config_entries.async_forward_entry_unload(config_entry, platform) for platform in PLATFORMS]
        )
    )
