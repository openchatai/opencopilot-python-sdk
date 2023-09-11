# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChatbotStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatbotStatus.DRAFT:
            return draft()
        if self is ChatbotStatus.PUBLISHED:
            return published()
        if self is ChatbotStatus.ARCHIVED:
            return archived()
