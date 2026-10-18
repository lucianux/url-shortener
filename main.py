import string
import random
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="URL Shortener API (In-Memory)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de datos en memoria (Diccionario de Python)
db = {}

class URLCreate(BaseModel):
    url: str

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

@app.post("/api/shorten", status_code=status.HTTP_201_CREATED)
def shorten_url(payload: URLCreate):
    code = generate_short_code()
    while code in db:
        code = generate_short_code()
        
    db[code] = {
        "target_url": payload.url,
        "clicks": 0
    }
    
    return {
        "short_code": code,
        "target_url": payload.url,
        "clicks": 0
    }

@app.get("/api/urls")
def list_urls():
    result = []
    for code, data in db.items():
        result.append({
            "short_code": code,
            "target_url": data["target_url"],
            "clicks": data["clicks"]
        })
    return result

@app.get("/{short_code}")
def redirect_to_url(short_code: str):
    if short_code not in db:
        raise HTTPException(status_code=404, detail="URL no encontrada")
    
    db[short_code]["clicks"] += 1
    
    return RedirectResponse(url=db[short_code]["target_url"], status_code=302)