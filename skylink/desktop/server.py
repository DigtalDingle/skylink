from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
import os
import subprocess
import socket
import pyautogui

app = FastAPI()

DEVICE_NAME = socket.gethostname()


@app.get("/status")
def status():
    return {"device": DEVICE_NAME, "status": "online"}


@app.get("/run-command")
def run_cmd(cmd: str):
    try:
        output = subprocess.check_output(cmd, shell=True, text=True)
        return {"output": output}
    except Exception as e:
        return {"error": str(e)}


@app.get("/list-files")
def list_files(path: str = "."):
    try:
        return {"files": os.listdir(path)}
    except Exception as e:
        return {"error": str(e)}


@app.get("/download")
def download(path: str):
    if os.path.exists(path):
        return FileResponse(path)
    return JSONResponse({"error": "File not found"}, status_code=404)


@app.get("/screenshot")
def screenshot():
    filepath = "desktop_screenshot.png"
    ss = pyautogui.screenshot()
    ss.save(filepath)
    return FileResponse(filepath)


@app.get("/open-rdp")
def open_rdp(target_ip: str):
    try:
        subprocess.Popen(f"mstsc /v:{target_ip}")
        return {"status": "RDP launched"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/shutdown")
def shutdown():
    os.system("shutdown /s /t 0")
    return {"status": "shutdown issued"}


@app.get("/reboot")
def reboot():
    os.system("shutdown /r /t 0")
    return {"status": "reboot issued"}
