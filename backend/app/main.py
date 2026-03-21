from fastapi import FastAPI
from openai import OpenAI

from app.routes import health, auth
from app.core.database import Base, engine
from app.models.user import User
from app.routes import ai
from app.models.material import Material
from fastapi.middleware.cors import CORSMiddleware
from app.routes import material

app = FastAPI(title="StudyAI API", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(health.router)
app.include_router(auth.router)

app.include_router(ai.router)

app.include_router(material.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode liberar geral por enquanto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(health.router)
app.include_router(material.router)
app.include_router(ai.router)
@app.get("/")
def root():
    return {"message": "StudyAI API is running 🚀"}