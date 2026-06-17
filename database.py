from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from os import getenv

engine = create_engine(f"{getenv('DB_URL')}")

LocalSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()