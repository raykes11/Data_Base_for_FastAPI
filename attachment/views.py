from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from attachment import crud
from attachment.dependencies import attachment_by_id
from attachment.schemas import (
    Attachment,
    AttachmentCreate,
    AttachmentUpdate,
    AttachmentUpdatePartial,
)

router = APIRouter(tags=["Attachments"])


@router.get("/", response_model=list[Attachment])
async def get_attachments(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_attachments(session)


@router.post(
    "/",
    response_model=Attachment,
    status_code=status.HTTP_201_CREATED,
)
async def create_attachment(
    attachment_in: AttachmentCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    print("__________________", attachment_in)
    return await crud.create_attachment(session=session, attachment_in=attachment_in)


@router.get("/{attachment_id}/", response_model=Attachment)
async def get_attachment(
    attachment: Attachment = Depends(attachment_by_id),
):
    return attachment


@router.put("/{attachment_id}/")
async def update_attachment(
    attachment_update: AttachmentUpdate,
    attachment: Attachment = Depends(attachment_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_attachment(
        session=session,
        attachment=attachment,
        attachment_update=attachment_update,
    )


@router.patch("/{attachment_id}/")
async def update_attachment_partial(
    attachment_update: AttachmentUpdatePartial,
    attachment: Attachment = Depends(attachment_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_attachment(
        session=session,
        attachment=attachment,
        attachment_update=attachment_update,
        partial=True,
    )


@router.delete("/{attachment_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_attachment(
    attachment: Attachment = Depends(attachment_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_attachment(session=session, attachment=attachment)
