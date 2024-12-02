from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .product import Product


class Attachment(Base):
    __tablename__ = "attachments"
    attachment_lv_1: Mapped[str]
    attachment_lv_2: Mapped[str] = mapped_column(nullable=True)
    attachment_lv_3: Mapped[str] = mapped_column(nullable=True)
    attachment_lv_4: Mapped[str] = mapped_column(nullable=True)
    attachment_lv_5: Mapped[str] = mapped_column(nullable=True)
    products: Mapped[list["Product"]] = relationship(back_populates="attachment")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, attachment={self.attachment_lv_1!r})"

    def __repr__(self):
        return str(self)
