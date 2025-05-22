# Centurion Garage Door Integration for Home Assistant

This is a custom integration for **Centurion Smart Garage Door Openers** that support local API access through the MY CGD App. It allows full control and monitoring of the garage door, internal lamp, vacation mode, and camera feed.

---

## ✅ Features

- 🚪 Open, close, and stop garage door
- 💡 Control garage lamp (on/off)
- 🏖 Enable or disable vacation mode
- 📷 View garage camera stream (`http://<ip>:88/`)
- ⚙️ Setup directly via Home Assistant UI (no YAML required)
- 🏠 HomeKit compatible through standard cover/switch/camera entities

---

## 📦 Installation

1. Download the [v0.9 initial release](https://github.com/andrew-snape/centurion-garage-HAS/releases)
2. Extract to your Home Assistant config:
   ```
   /config/custom_components/centurion/
   ```
3. Restart Home Assistant.

---

## Configuration

Go to **Settings → Devices & Services → Add Integration**, then search for **Centurion**. Enter your device's IP and local API key from the MY CGD app.

---

## 📜 License

MIT License

---

Developed by [Andrew Snape](https://github.com/andrew-snape)
