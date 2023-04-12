# coding: utf-8

"""
    Stream Video API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v79.46.0-2-gc33e7ee4e
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stream.model import schemas  # noqa: F401


class CallMemberAddedEvent(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This event is sent when one or more members are added to a call
    """

    class MetaOapg:
        required = {
            "call",
            "call_cid",
            "members",
            "created_at",
            "type",
        }

        class properties:
            @staticmethod
            def call() -> typing.Type["CallResponse"]:
                return CallResponse

            call_cid = schemas.StrSchema
            created_at = schemas.DateTimeSchema

            class members(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["MemberResponse"]:
                        return MemberResponse

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["MemberResponse"], typing.List["MemberResponse"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "members":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> "MemberResponse":
                    return super().__getitem__(i)

            type = schemas.StrSchema
            __annotations__ = {
                "call": call,
                "call_cid": call_cid,
                "created_at": created_at,
                "members": members,
                "type": type,
            }

    call: "CallResponse"
    call_cid: MetaOapg.properties.call_cid
    members: MetaOapg.properties.members
    created_at: MetaOapg.properties.created_at
    type: MetaOapg.properties.type

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["call"]) -> "CallResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["members"]
    ) -> MetaOapg.properties.members:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call",
                "call_cid",
                "created_at",
                "members",
                "type",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["call"]) -> "CallResponse":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["members"]
    ) -> MetaOapg.properties.members:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call",
                "call_cid",
                "created_at",
                "members",
                "type",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        call: "CallResponse",
        call_cid: typing.Union[
            MetaOapg.properties.call_cid,
            str,
        ],
        members: typing.Union[
            MetaOapg.properties.members,
            list,
            tuple,
        ],
        created_at: typing.Union[
            MetaOapg.properties.created_at,
            str,
            datetime,
        ],
        type: typing.Union[
            MetaOapg.properties.type,
            str,
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "CallMemberAddedEvent":
        return super().__new__(
            cls,
            *_args,
            call=call,
            call_cid=call_cid,
            members=members,
            created_at=created_at,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )


from stream.model.call_response import CallResponse
from stream.model.member_response import MemberResponse
