from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.core.database import Base

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    summary = Column(Text)
    flashcards = Column(Text)
    quiz = Column(Text)