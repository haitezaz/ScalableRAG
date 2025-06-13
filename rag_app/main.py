# rag_app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from rag_app.pipeline import chain
import os

app = FastAPI()

# Point to templates folder OUTSIDE rag_app/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Optional: if you have a static folder, mount it like this
# app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/ask", response_class=HTMLResponse)
async def ask_form(request: Request, query: str = Form(...)):
    try:
        result = chain.invoke(query)
        return templates.TemplateResponse("index.html", {"request": request, "response": result})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "response": f"Error: {str(e)}"})

class QueryRequest(BaseModel):
    query: str

@app.post("/ask-json")
async def ask_json(payload: QueryRequest):
    try:
        result = chain.invoke(payload.query)
        return {"response": result}
    except Exception as e:
        return {"response": "Sorry, an error occurred.", "error": str(e)}
