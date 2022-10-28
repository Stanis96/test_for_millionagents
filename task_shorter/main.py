import secrets

import validators
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import models, plans
from .db import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def start_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def handle_exception(request, message):
    message = f"Данный URL '{request.url}'не существует"
    raise HTTPException(status_code=400, detail=message)


@app.get("/")
def main_page():
    return "The main page of Shorter"


@app.get("/{url_key}")
def get_aim_url(url_key: str, request: Request, db: Session = Depends(start_db)):
    db = db.query(models.URL).filter(models.URL.key == url_key, models.URL.status).first()
    if db:
        return RedirectResponse(db.aim_url)
    else:
        handle_exception(request)


@app.post("/url", response_model=plans.URLInfo)
def create_url(url: plans.URLBase, db: Session = Depends(start_db)):
    if not validators.url(url.aim_url):
        handle_exception(message="Данный URL-адрес недействителен")

    chars = "1Q2W3E4R5T6Y7U8I9O0PASDFGHJKLZXCVBNM"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db = models.URL(aim_url=url.aim_url, key=key, secret_key=secret_key)
    db.add(db)
    db.commit()
    db.refresh(db)
    db.url = key
    db.admin_url = secret_key
    return db
