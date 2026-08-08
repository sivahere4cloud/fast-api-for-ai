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

"""
@app.post("/chat")
def chat(request: ChatRequest):
    return{
        "recived":request.message,
        "model": request.model,
        "temperature": request.temperature
    }
"""

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







