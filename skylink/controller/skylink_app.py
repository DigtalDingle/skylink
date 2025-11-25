from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx

DESKTOP_IP = "100.111.3.101:8001"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


async def get_status():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"http://{DESKTOP_IP}/status")
            return r.json()
    except:
        return {"device": "Desktop", "status": "offline"}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    status = await get_status()
    return templates.TemplateResponse("index.html",
                                      {"request": request, "status": status})
