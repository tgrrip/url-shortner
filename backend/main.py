import secrets
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime, timedelta

app = FastAPI()

# --- Настройка CORS ---
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- "База данных" в памяти (словарь Python) ---
# Ключ - короткий код, значение - длинный URL
url_db = {}

# --- Pydantic модели ---
class URLCreate(BaseModel):
    long_url: HttpUrl # Pydantic проверит, что это валидный URL
    custom_code: Optional[str] = None

# --- Эндпоинты API ---

@app.post("/api/shorten")
def create_short_url(url_data: URLCreate, request: Request):
    """Создает короткий код для длинного URL."""
    long_url = str(url_data.long_url)
    custom_code = url_data.custom_code

    if custom_code:
        short_code = custom_code
        if short_code in url_db:
            raise HTTPException(status_code=400, detail="!")
    else:
        short_code = secrets.token_urlsafe(6)
        while short_code in url_db:
            short_code = secrets.token_urlsafe(6)
    
    url_db[short_code] = {
        "long_url": long_url,
        "clicks": 0,
        "created_at": datetime.utcnow()
    }

    # Формируем полный короткий URL для ответа
    base_url = str(request.base_url)
    short_url = f"{base_url}{short_code}"

    return {"short_url": short_url, "clicks": 0}

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str):
    """Ищет длинный URL по короткому коду и перенаправляет на него."""
    entry = url_db.get(short_code)
    if not entry:
        raise HTTPException(status_code=404, detail="Short URL not found")
    created_at = entry["created_at"]
    if datetime.utcnow() - created_at > timedelta(days=7):
        raise HTTPException(status_code=404, detail="Срок действия ссылки истек")
    
    entry["clicks"] += 1

    # Выполняем HTTP 307 Temporary Redirect
    return RedirectResponse(url=entry["long_url"])