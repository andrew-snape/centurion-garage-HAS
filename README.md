# Centurion Garage Door Integration for Home Assistant

This is a custom integration for **Centurion Smart Garage Door Openers** that support the **local API** available through the MY CGD app.

It enables control and monitoring of:
- 🚪 Garage Door (open, close, stop)
- 💡 Lamp (on/off)
- 🏖 Vacation Mode (on/off)
- 📷 Camera Stream (MJPEG, via `http://<ip>:88/`)

---

## 📦 Installation via HACS

### Step 1: Add Repository
1. Go to **HACS → Integrations → ⋮ (three dots) → Custom repositories**
2. Paste this URL: `https://github.com/andrew-snape/centurion-garage-HAS`
3. Choose category: `Integration`
4. Click "Add"

### Step 2: Install the Integration
1. Go to **HACS → Integrations**
2. Search for **Centurion Garage Door**
3. Click **Download**

### Step 3: Restart Home Assistant

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **Centurion**
3. Enter:
   - `IP Address`: The IP of your Centurion controller (e.g., `192.168.0.8`)
   - `API Key`: The local API key from the MY CGD app

No YAML is required. All setup is done through the Home Assistant UI.

---

## 🧩 Entities Created

| Entity Type | Name                    | Entity ID Example                  |
|-------------|-------------------------|------------------------------------|
| `cover`     | Centurion Garage Door   | `cover.centurion_garage_door`     |
| `switch`    | Centurion Lamp          | `switch.centurion_garage_lamp`    |
| `switch`    | Vacation Mode           | `switch.centurion_vacation_mode`  |
| `camera`    | Garage Camera           | `camera.centurion_garage_camera`  |

---

## 🧪 Troubleshooting

- Test the camera stream at `http://<your-ip>:88/`
- Ensure the IP is reachable locally and the API key is correct
- Use a **static IP** for your garage controller to avoid reconnection issues

---

## 📜 License

MIT

---

## 🙌 Credits

Developed by [Andrew Snape](https://github.com/andrew-snape)  
Not affiliated with Centurion or CGD.
