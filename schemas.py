from pydantic import BaseModel, Field

# --- Pydantic schemas for validation and serialization ---

class ItemCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str | None = None
    price: float = Field(gt=0)



class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str | None = None

class ItemUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str | None = None
    price: float = Field(gt=0)

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=32)
    email: str = Field(min_length=5, max_length=100)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    class Config:         
        from_attributes = True


