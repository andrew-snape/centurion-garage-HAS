import asyncio

from .const import DOMAIN

PLATFORMS = ["cover", "switch"]


async def async_setup_entry(hass, config_entry):
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True


async def async_unload_entry(hass, config_entry):
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
