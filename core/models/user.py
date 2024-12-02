from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship


from .base import Base

if TYPE_CHECKING:
    from .order import Order


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(unique=True)
    address: Mapped[str]
    email: Mapped[str]
    orders: Mapped[list["Order"]] = relationship(back_populates="user")
