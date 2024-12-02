from pydantic import BaseModel, ConfigDict


class AttachmentBase(BaseModel):
    attachment_lv_1: str
    attachment_lv_2: str
    attachment_lv_3: str
    attachment_lv_4: str
    attachment_lv_5: str


class AttachmentCreate(AttachmentBase):
    pass


class AttachmentUpdate(AttachmentCreate):
    pass


class AttachmentUpdatePartial(AttachmentCreate):
    attachment_lv_1: str | None = None
    attachment_lv_2: str | None = None
    attachment_lv_3: str | None = None
    attachment_lv_4: str | None = None
    attachment_lv_5: str | None = None


class Attachment(AttachmentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
