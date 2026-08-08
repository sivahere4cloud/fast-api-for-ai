from  pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    model: str
    temperature: float

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    