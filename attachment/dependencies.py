from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Product
from attachment import crud


async def attachment_by_id(
        attachment_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    attachment = await crud.get_attachment(session=session, attachment_id=attachment_id)
    if attachment is not None:
        return attachment

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Product {attachment_id} not found!',
    )
