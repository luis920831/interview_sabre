from fastapi import FastAPI, Depends
from schema.Book import Book as BookSchema
from schema.User import User as UserSchema
from sqlalchemy.orm import Session
from db import create_db, get_db, Book, User, Book_user

app = FastAPI()

create_db()

@app.post("/book/", response_model=BookSchema)
def save_book(data: BookSchema, db: Session = Depends(get_db)):
    return create_book(data, db)

@app.post("/user/", response_model=UserSchema)
def save_user(data: UserSchema, db: Session = Depends(get_db)):
    return create_user(data, db)

@app.get("/get_books_user/{id}")
def get_books(id: int, db: Session = Depends(get_db)):
    return books_user(id, db)


def create_book(data: BookSchema, db: Session):
    print(data.__dict__)

    book = Book(title=data.title, author=data.author, available = data.available)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def create_user(data: UserSchema, db: Session):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def books_user(userid, db: Session):
    books = db.query(Book_user).filter(Book_user.id_user==userid).all()
    return books



