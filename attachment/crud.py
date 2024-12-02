from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Attachment
from sqlalchemy import select
from sqlalchemy.engine import Result

from attachment.schemas import (
    AttachmentCreate,
    AttachmentUpdate,
    AttachmentUpdatePartial,
)


async def get_attachments(session: AsyncSession) -> list[Attachment]:
    quality_set = select(Attachment).order_by(Attachment.id)
    result: Result = await session.execute(quality_set)
    attachments = result.scalars().all()
    return list(attachments)


async def get_attachment(
    session: AsyncSession, attachment_id: int
) -> Attachment | None:
    return await session.get(Attachment, attachment_id)


async def create_attachment(
    session: AsyncSession, attachment_in: AttachmentCreate
) -> Attachment:
    attachment = Attachment(**attachment_in.model_dump())
    session.add(attachment)
    await session.commit()
    return attachment


async def update_attachment(
    session: AsyncSession,
    attachment: Attachment,
    attachment_update: AttachmentUpdate | AttachmentUpdatePartial,
    partial: bool = False,
) -> Attachment:
    for name, value in attachment_update.model_dump(exclude_unset=partial).items():
        setattr(attachment, name, value)
    await session.commit()
    return attachment


async def delete_attachment(
    session: AsyncSession,
    attachment: Attachment,
) -> None:
    await session.delete(attachment)
    await session.commit()
