from sqlalchemy import create_engine, Column, String, Integer
import sqlalchemy
from sqlalchemy.orm import sessionmaker, session

engine = create_engine("sqlite:///./database.db")
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = "user"
    id=Column(Integer, primary_key=True)
    name=Column(String)


class Book(Base):
    __tablename__ = "book"
    id=Column(Integer, primary_key=True)
    title=Column(String)
    author=Column(String)
    available=Column(Integer)
    
class Book_user(Base):
    __tablename__ = "book_user"
    id=Column(Integer, primary_key=True)
    id_user=Column(Integer)
    id_book=Column(Integer)


def create_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()