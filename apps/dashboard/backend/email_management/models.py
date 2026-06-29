from pydantic import BaseModel


class ActionStatusUpdate(BaseModel):
    status: str
    name: str | None = None
    event_datetime: str | None = None


class ActionCreate(BaseModel):
    type: str
    name: str | None = None
    event_datetime: str | None = None


class DisposeRequest(BaseModel):
    action: str
