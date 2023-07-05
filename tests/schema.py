from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    home_folder_id: UUID
    inbox_folder_id: UUID


class OCRStatusEnum(str, Enum):
    unknown = 'UNKNOWN'
    received = 'RECEIVED'
    started = 'STARTED'
    success = 'SUCCESS'
    failed = 'FAILED'


class NodeType(str, Enum):
    document = "document"
    folder = "folder"


class DocumentNode(BaseModel):
    """Minimalist part of the document returned as part of nodes list"""
    ocr: bool = True  # will this document be OCRed?
    ocr_status: OCRStatusEnum = OCRStatusEnum.unknown


class Tag(BaseModel):
    name: str
    color: str


class Node(BaseModel):
    id: UUID
    title: str
    ctype: NodeType
    tags: List[Tag]
    created_at: datetime
    updated_at: datetime
    parent_id: UUID | None
    user_id: UUID
    document: DocumentNode | None = None

    @validator('document', pre=True)
    def document_validator(cls, value, values):
        if values['ctype'] == NodeType.document:
            return DocumentNode(
                ocr_status=value['ocr_status'],
                ocr=value['ocr']
            )

        return None
