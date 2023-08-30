#Now create Pydantic models (schemas) that will be used when reading data, when returning it from the API.
#Pydantic models are Python classes used for data validation and serialization,automatic datatype conversion
#before it's used in applications, such as web APIs. 
#Pydantic models declare the types using :, the new type annotation syntax/type hints: name: str


from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
    
    # orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
