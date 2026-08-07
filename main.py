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








