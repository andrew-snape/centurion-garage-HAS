# Centurion Garage Door Integration for Home Assistant

A custom integration for controlling Centurion smart garage doors and accessories via the local API.

**What's new in 0.9.6:**  
- State for lamp, vacation, and door syncs automatically from controller API
- Entity icons and device info
- Door entity maps open/closed/opening/closing/stopped/error correctly for Home Assistant
- Configurable polling interval (default 30s)

## Features
- Open, close, and stop the garage door
- Toggle lamp and vacation mode
- All configuration through Home Assistant UI (no YAML required)
- Reliable local control (no cloud, no camera, no HACS)

## How to install
1. Copy `custom_components/centurion/` to your Home Assistant config folder.
2. Restart Home Assistant.
3. Add the Centurion integration via "Devices & Services".

MIT License — Developed by Andrew Snape
