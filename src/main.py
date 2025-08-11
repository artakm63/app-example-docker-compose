from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from database import create_tables
from repository import get_dog_repository, DogRepository
from schemas import DogCreate, DogRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/dog/{id}", response_model=DogRead)
async def get_a_dog(id: str, dog_repo: DogRepository = Depends(get_dog_repository)) -> DogRead:
    dog = await dog_repo.get_dog_by_id(id)
    if dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dog


@app.post("/dog", response_model=DogRead, status_code=201)
async def create_dog(dog: DogCreate, dog_repo: DogRepository = Depends(get_dog_repository)) -> DogRead:
    new_dog = await dog_repo.create_dog(dog)
    return new_dog


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
