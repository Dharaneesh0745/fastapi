from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    pages: int
    description: str = None
    
books: List[Book] = []

@app.get("/")
def test():
    return {"message": "Hello, World!"}

@app.post("/add-book", response_model=Book)
def add_book(book: Book):
    
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this id already exists!")
    
    books.append(book)
    return {"message": "Book added successfully!", "data": book}

@app.get("/get-all-books", response_model=List[Book])
def get_all_books():
    return books
