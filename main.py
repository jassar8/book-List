from fastapi import FastAPI, HTTPException 
 
app = FastAPI() 
 
# "ןורכיזב "םינותנ דסמ 
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 3, "title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki"},
    {"id": 4, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 5, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"}
]
counter = 6
 
@app.get("/books") 
def get_books(): 
    return books 
 
@app.get("/books/{book_id}") 
def get_book(book_id: int): 
    for book in books: 
        if book["id"] == book_id: 
            return book 
    raise HTTPException(status_code=404, detail="Book not found") 
 
@app.post("/books") 
def add_book(book: dict): 
    global counter 
    new_book = { 
        "id": counter, 
     "title": book.get("title"), 
        "author": book.get("author") 
    } 
    books.append(new_book) 
    counter += 1 
    return new_book 
 
@app.delete("/books/{book_id}") 
def delete_book(book_id: int): 
    for book in books: 
        if book["id"] == book_id: 
            books.remove(book) 
            return {"message": "Book deleted"} 
    raise HTTPException(status_code=404, detail="Book not found")
