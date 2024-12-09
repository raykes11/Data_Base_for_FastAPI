from typing import TYPE_CHECKING, Dict

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableDict

from .base import Base

if TYPE_CHECKING:
    from .attachment import Attachment
    from .order import Order
    from .order_product_association import OrderProductAssociation


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str]
    price: Mapped[int] = mapped_column(default=100, server_default="100")
    count: Mapped[int]
    property: Mapped[Dict] = mapped_column(HSTORE)
    attachment_id: Mapped[int | None] = mapped_column(ForeignKey("attachments.id"))

    attachment: Mapped["Attachment"] = relationship(back_populates="products")
    orders: Mapped[list["Order"]] = relationship(
        secondary="order_product_user_association", back_populates="products"
    )
    orders_details: Mapped[list["OrderProductUserAssociation"]] = relationship(
        back_populates="product"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, product={self.name!r})"

    def __repr__(self):
        return str(self)
