from fastapi import Depends
from sqlalchemy import insert, select

from database import get_session
from schemas import DogCreate, DogRead
from models import Dog as DatabaseDog


class DogRepository:
    def __init__(self, database_session):
        self.database_session = database_session

    async def create_dog(self, data: DogCreate) -> DatabaseDog:
        dog_as_dict = data.model_dump()
        insert_stmt = insert(DatabaseDog).values(**dog_as_dict).returning(DatabaseDog)
        result = await self.database_session.execute(insert_stmt)
        await self.database_session.commit()
        return result.scalars().one()


    async def get_dog_by_id(self, dog_id: str) -> DogRead | None:
        dog_stmt = select(DatabaseDog).where(DatabaseDog.id == dog_id)
        dog_data = await self.database_session.execute(
            dog_stmt
        )
        dog = dog_data.scalars().one_or_none()
        if dog is None:
            return None

        validated_dog = DogRead.model_validate(dog)
        return validated_dog


async def get_dog_repository(db_session = Depends(get_session)):
    return DogRepository(db_session)
