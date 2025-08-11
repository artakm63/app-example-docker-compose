from pydantic import BaseModel


class DogBase(BaseModel):
    name: str
    age: int
    breed: str
    owner_name: str


class DogCreate(DogBase):
    pass


class DogRead(DogBase):
    id: str

    class Config:
        from_attributes = True
