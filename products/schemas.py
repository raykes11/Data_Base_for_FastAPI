from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    prise: int
    count: int
    property: str
    attachment_id: int | None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    prise: int | None = None
    count: int | None = None
    property: str | None = None
    attachment_id: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
