from fastapi import APIRouter
from app.services.ai_service import (
    generate_summary,
    generate_flashcards,
    generate_quiz
)


router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/summary")
def summary(text: str):
    return {"summary": generate_summary(text)}


@router.post("/flashcards")
def flashcards(text: str):
    return {"flashcards": generate_flashcards(text)}


@router.post("/quiz")
def quiz(text: str):
    return {"quiz": generate_quiz(text)}

