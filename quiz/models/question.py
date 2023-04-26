from database import db
from sqlalchemy import sql
from sqlalchemy import Column, Integer, String, JSON


class QuestionModel(db.Base):
    """
    Model class for representing questions and their answers in a database.
    """
    __tablename__ = "Question model"

    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    id = Column(
        Integer,
        primary_key=True,
    )

    question = Column(
        String(500),
        nullable=False,
    )

    answers = Column(
        JSON,
        nullable=False
    )

    correct_answer = Column(
        String(1),
        nullable=False
    )

    @classmethod
    def read(cls):
        stmt = sql.select(cls)
        question = db.session.execute(stmt).fetchmany()
        return question

    @classmethod
    def create(cls, question, answers, correct_answer):
        question = cls(
            question=question,
            answers=answers,
            correct_answer=correct_answer
            )
        db.session.add(question)
        db.session.commit()
        return question
    

    @classmethod
    def delete(cls, id):
        stmt = sql.delete(cls).where(cls.id == id)
        db.session.execute(stmt)
        db.session.commit()

    def __str__(self):
        return self.question
    
    def __repr__(self):
        return self.question