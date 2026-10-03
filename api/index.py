import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Hub de Inteligência Financeira para Delivery")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Captura a raiz (/) e qualquer reescrita enviada pela Vercel (/api, /api/index.py, etc.)
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def render_dashboard(request: Request, full_path: str = ""):
    return templates.TemplateResponse("index.html", {"request": request})
