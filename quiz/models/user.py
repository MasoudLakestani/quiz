from database import db
from sqlalchemy import sql
from sqlalchemy import Column, Integer, String, Boolean


class UserModel(db.Base):
    """
    Model class for representing user in a database.
    """
    __tablename__ = "auth user model"

    def __init__(self, username, password, is_superuser):
        self.username = username
        self.password = password
        self.is_superuser = is_superuser
    id = Column(
        Integer,
        primary_key=True,
    )

    username = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    is_superuser = Column(
        Boolean,
        default=False
    )

    @classmethod
    def read(
        cls,
        username
        ):
        stmt = sql.select(cls).where(cls.username == username)
        user = db.session.execute(stmt).one_or_none()
        return user

    @classmethod
    def create(
        cls,
        username,
        password,
        is_superuser
        ):
        user = cls(
            username=username,
            password=password,
            is_superuser=is_superuser
            )
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def update_username(
        cls,
        old_username,
        new_username
        ):
        stmt = (
            sql.update(cls)
            .where(cls.username == old_username)
            .values(username=new_username)
        )
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def update_password(
        cls,
        old_password,
        new_password
        ):
        stmt = (
            sql.update(cls)
            .where(cls.password == old_password)
            .values(password=new_password)
        )
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def delete(
        cls,
        username
        ):
        stmt = sql.delete(cls).where(cls.username == username)
        db.session.execute(stmt)
        db.session.commit()

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"{self.username}"

