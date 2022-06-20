# generated by datamodel-codegen:
#   filename:  storage_blob_created.json
#   timestamp: 2022-06-20T07:55:08+00:00

from __future__ import annotations
from az_evgrid_pydantic_schema.base import Base
from pydantic import BaseModel


class StorageDiagnostics(BaseModel):
    batchId: str


class StorageBlobCreatedBase(BaseModel):
    api: str
    clientRequestId: str
    requestId: str
    eTag: str
    contentType: str
    contentLength: int
    blobType: str
    url: str
    sequencer: str
    storageDiagnostics: StorageDiagnostics


class StorageBlobCreatedFull(Base):
    data: StorageBlobCreatedBase
