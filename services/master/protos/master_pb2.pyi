from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageRequest(_message.Message):
    __slots__ = ("id", "message", "user_id", "channel_id", "create_at", "update_at", "root_id", "edit_at", "delete_at", "is_pinned", "original_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    EDIT_AT_FIELD_NUMBER: _ClassVar[int]
    DELETE_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    message: str
    user_id: int
    channel_id: int
    create_at: int
    update_at: int
    root_id: int
    edit_at: int
    delete_at: int
    is_pinned: bool
    original_id: int
    def __init__(self, id: _Optional[int] = ..., message: _Optional[str] = ..., user_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., create_at: _Optional[int] = ..., update_at: _Optional[int] = ..., root_id: _Optional[int] = ..., edit_at: _Optional[int] = ..., delete_at: _Optional[int] = ..., is_pinned: bool = ..., original_id: _Optional[int] = ...) -> None: ...

class MessageRespons(_message.Message):
    __slots__ = ("id", "message", "user_id", "channel_id", "create_at", "update_at", "root_id", "edit_at", "delete_at", "is_pinned", "original_id", "respons_message", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    EDIT_AT_FIELD_NUMBER: _ClassVar[int]
    DELETE_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    message: str
    user_id: int
    channel_id: int
    create_at: int
    update_at: int
    root_id: int
    edit_at: int
    delete_at: int
    is_pinned: bool
    original_id: int
    respons_message: str
    status: str
    def __init__(self, id: _Optional[int] = ..., message: _Optional[str] = ..., user_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., create_at: _Optional[int] = ..., update_at: _Optional[int] = ..., root_id: _Optional[int] = ..., edit_at: _Optional[int] = ..., delete_at: _Optional[int] = ..., is_pinned: bool = ..., original_id: _Optional[int] = ..., respons_message: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class CreateMessageRespons(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
