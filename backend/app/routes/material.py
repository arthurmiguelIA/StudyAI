from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.material import Material
from app.services.ai_service import generate_summary, generate_flashcards, generate_quiz
from app.schemas.material import MaterialCreate
from app.core.security import get_current_user

router = APIRouter(prefix="/materials", tags=["Materials"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    @router.post("/")
    def create_material(data: MaterialCreate, db: Session = Depends(get_db)):
        text = data.text

        summary = generate_summary(text)
        flashcards = str(generate_flashcards(text))
        quiz = str(generate_quiz(text))

        new_material = Material(
            user_id=1,
            content=text,
            summary=summary,
            flashcards=flashcards,
            quiz=quiz
        )

        db.add(new_material)
        db.commit()
        db.refresh(new_material)

        return new_material

@router.get("/")
def get_materials(db: Session = Depends(get_db)):
    return db.query(Material).all()
@router.post("/")
def create_material(data: MaterialCreate, db: Session = Depends(get_db)):
    text = data.text

    summary = generate_summary(text)
    flashcards = str(generate_flashcards(text))
    quiz = str(generate_quiz(text))

    new_material = Material(
        user_id=1,
        content=text,
        summary=summary,
        flashcards=flashcards,
        quiz=quiz
    )

    db.add(new_material)
    db.commit()
    db.refresh(new_material)

    return new_material

@router.post("/")
def create_material(
    data: MaterialCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  # 🔥 aqui
):
    text = data.text

    summary = generate_summary(text)

    new_material = Material(
        user_id=user.id,  # 🔥 agora é real
        content=text,
        summary=summary,
        flashcards="",
        quiz=""
    )

    db.add(new_material)
    db.commit()
    db.refresh(new_material)

    return new_material