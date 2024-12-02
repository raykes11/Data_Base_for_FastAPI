from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .attachment import Attachment
    from .order import Order
    from .order_product_user_association import OrderProductUserAssociation


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str]
    price: Mapped[int] = mapped_column(default=100, server_default="100")
    count: Mapped[int]
    property: Mapped[str]
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
