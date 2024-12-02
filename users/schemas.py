from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    address: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    name: str | None = None
    address: str | None = None
    email: str | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
