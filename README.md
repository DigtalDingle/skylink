# SkyLink – Secure Phone-to-Desktop Control System

SkyLink is a lightweight remote dashboard that lets you control or monitor a desktop computer directly from your phone over **Tailscale**.  
It uses **FastAPI** for both the device agent and the controller dashboard.

This project is the groundwork for future automation concepts — including remote cat-feeding, device actions, and more.

---

## 🚀 Features (v1)

- Secure, private communication using Tailscale
- Desktop “agent” server that exposes a simple `/status` API
- Controller dashboard with a clean HTML/CSS UI
- Phone-accessible dashboard (mobile friendly)
- Modular structure for future builds and expansions

---

## 📁 Project Structure

SkyLink/
│
├── controller/ # Phone-facing UI/dashboard
│ ├── skylink_app.py
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ │ └── style.css
│ ├── devices.json
│ └── requirements.txt
│
├── desktop/ # Device agent
│ ├── server.py
│ └── requirements.txt
│
└── README.md
