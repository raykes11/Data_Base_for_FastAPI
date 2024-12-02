from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from .base import Base

if TYPE_CHECKING:
    from .product import Product
    from .order_product_user_association import OrderProductUserAssociation
    from .user import User


class Order(Base):
    __tablename__ = "orders"
    promocode: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), default=1, server_default="1"
    )
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_user_association", back_populates="orders"
    )
    # association between Order -> Association -> Product
    products_details: Mapped[list["OrderProductUserAssociation"]] = relationship(
        back_populates="order"
    )
    user: Mapped["User"] = relationship(back_populates="orders")
