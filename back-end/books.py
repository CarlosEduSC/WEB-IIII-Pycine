import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/book/{id}")
def get_book_by_id(id: int):
    with open("books.json") as f:
        data = json.load(f)

        for item in data:
            if item['id'] == id:
                return item
            
@app.get("/book/year/{ano}")
def get_book_by_year(ano:int):
    with open("books.json") as f:
        data = json.load(f)

        livros = []

        for item in data:
            if item['year'] == ano:
                livros.insert(item['id'], item)
        
        return livros
    
@app.get("/book/title/{titulo}")
def get_book_by_title(titulo):
    with open("books.json") as f:
        data = json.load(f)

        for item in data:
            if item['title'] == titulo:
                return item
            
@app.get("/book/author/{autor}")
def get_book_by_author(autor):
    with open("books.json") as f:
        data = json.load(f)

        livros = []

        for item in data:
            for author in item['authors']:
                author = author.lower().replace(" ", "")
                autor = autor.lower().replace(" ", "")
                if autor in author:
                    livros.insert(item['id'], item)

        return livros