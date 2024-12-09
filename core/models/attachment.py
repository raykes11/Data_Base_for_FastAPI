from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .product import Product


class Attachment(Base):
    __tablename__ = "attachments"
    name: Mapped[str]
    parent_id: Mapped[int| None]
    products: Mapped[list["Product"]] = relationship(back_populates="attachment")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, attachment={self.attachment!r})"

    def __repr__(self):
        return str(self)


