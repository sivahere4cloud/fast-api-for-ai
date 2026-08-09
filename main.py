
"""
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to fast Api for AI learning"
##path vs query 
#Path Parameter

#A path parameter identifies one specific resource.
# 
# query parameters
#A query parameter filters or modifies the result.


documents = [
    {"id": 1, "title": "FastAPI Guide", "category": "backend", "author": "Siva"},
    {"id": 2, "title": "LangChain Basics", "category": "ai", "author": "John"},
    {"id": 3, "title": "RAG Systems", "category": "ai", "author": "Siva"},
]

@app.get("/documents/search")
def search_documents(category: str,author: str):
    results = []

    for document in documents:
        if (
            document["category"] == category
            and document["author"] == author
        ):
            results.append(document)

    return results

#path based parameter
@app.get("/documents/{document_id}")#Here we are requesting  one specific document
def get_document(document_id: int):
    for document in documents:
        if document["id"] == document_id:
            return document

    return "Document Not found"


#Query Based Parameter
@app.get("/documents") #here we are rquesting to filter ai category from the data..
def get_documents(category: str):
    results = []

    for document in documents:
        if document["category"] == category:
            results.append(document)

    return results

##Multiple query parameteres
@app.get("/documents/search")
def search_documents(
    category: str,
    author: str
):
    results = []

    for document in documents:
        if (
            document["category"] == category
            and document["author"] == author
        ):
            results.append(document)

    return results

## Request Body (Pydantic Models)
#This is one of the most important topics because every AI application receives data from users.

#create a pydantic model


from models import ChatRequest,UserResponse


@app.post("/chat")
def chat(request: ChatRequest):
    return{
        "recived":request.message,
        "model": request.model,
        "temperature": request.temperature
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": f"You asked: {request.message}",
        "model": request.model,
        "temperature": request.temperature
    }

##Response Models
#================

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "username": "siva",
        "email": "siva@gmail.com",
        "password": "secret123"
    }

##Status Codes
from fastapi import HTTPException

@app.get("/student/{id}")
def get_student(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"id": 1, "name": "Siva"}


#Dependency Injection(Depends)
#If you master Depends, you'll understand how production FastAPI applications are built.

from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Depends
from sqlalchemy.orm import Session

@app.get("/users")
def get_users(db:Session = Depends(get_db)):
    return db.query(User).all
"""
#Asynv vs Sync

from fastapi import FastAPI,Request
import asyncio
app =FastAPI()

@app.get("/")
def hello():
    return {"Message": "Hello"}


#Asynchronous

@app.get("/asynco")
async def greet():
    await asyncio.sleep(5)
    return {"message": "Hello"}

#Middleware :: Middleware is code that runs before and after every request.


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("Before Request")

    response = await call_next(request)

    print("After Request")

    return response

@app.get("/")
def home():
    return {"message": "Hello"}

#Exception handling

@app.get("/products/{id}")
def get_product(id: int):
    return products[id]

from fastapi import HTTPException

@app.get("/products/{id}")
def get_product(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "id": 1,
        "name": "Laptop"
    }




@app.get("/student/{id}")
def get_student(id: int):

    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": 1,
        "name": "Siva"
    }


#Background Tasks
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email(email: str):
    print(f"Sending email to {email}")

@app.post("/register")
def register(email: str, background_tasks: BackgroundTasks):

    background_tasks.add_task(send_email, email)

    return {"message": "User registered successfully"}


#Mini Exercise
from fastapi import BackgroundTasks

def log_message():
    print("Background task executed")

@app.get("/background")
def background(background_tasks: BackgroundTasks):

    background_tasks.add_task(log_message)

    return {"message": "Response returned immediately"}

