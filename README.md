# Centurion Garage Door Integration for Home Assistant

This is a custom integration for controlling **Centurion smart garage doors** using the **local API** available via the MY CGD app.

It allows local, cloud-free control of:
- 🚪 Garage door (open, close, stop)
- 💡 Internal lamp
- 🏖 Vacation mode
- 📷 MJPEG camera stream (from port `88`)

---

## ✅ Features

- Control your garage door directly from Home Assistant
- Toggle the Centurion lamp and vacation mode
- View the built-in camera stream via MJPEG
- UI-based setup — **no YAML required**
- Local API — no cloud services or internet dependency

---

## 🧩 Entities Created

| Entity Type | Description              | Example Entity ID                  |
|-------------|--------------------------|------------------------------------|
| `cover`     | Garage door              | `cover.centurion_garage_door`     |
| `switch`    | Internal lamp            | `switch.centurion_garage_lamp`    |
| `switch`    | Vacation mode            | `switch.centurion_vacation_mode`  |
| `camera`    | MJPEG stream (port 88)   | `camera.centurion_garage_camera`  |

---

## 📦 Installation via HACS

### Step 1: Add as a Custom Repository
1. In Home Assistant, go to **HACS → Integrations → ⋮ → Custom repositories**
2. Enter the repo URL:
