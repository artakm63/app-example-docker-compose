import uuid

from sqlalchemy import Column, Integer, String

from database import Base


def dog_id_default():
    dog_id = uuid.uuid4()
    return str(dog_id)


class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(String(36), primary_key=True, default=dog_id_default)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    breed = Column(String(50), nullable=False)
    owner_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Dog(name='{self.name}', age={self.age}, breed='{self.breed}', owner_name='{self.owner_name}'>"
