from pydantic import BaseModel, ConfigDict


class AttachmentBase(BaseModel):
    # id: int
    name: str
    parent_id: int # add id Attachment


class AttachmentCreate(AttachmentBase):
    pass


class AttachmentUpdate(AttachmentCreate):
    pass


class AttachmentUpdatePartial(AttachmentCreate):
    name: str | None
    parent_id: int | None


class Attachment(AttachmentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
