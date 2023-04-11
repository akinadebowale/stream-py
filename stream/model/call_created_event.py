# coding: utf-8

"""
    Stream Video API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v79.45.0
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

from model import schemas  # noqa: F401


class CallCreatedEvent(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
        Ref: https://openapi-generator.tech

        Do not edit the class manually.

        This event is sent when a call is created. Clients receiving this event should check if the ringing
    field is set to true and if so, show the call screen
    """

    class MetaOapg:
        required = {
            "call",
            "ringing",
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

            ringing = schemas.BoolSchema
            type = schemas.StrSchema
            __annotations__ = {
                "call": call,
                "call_cid": call_cid,
                "created_at": created_at,
                "members": members,
                "ringing": ringing,
                "type": type,
            }

    call: "CallResponse"
    ringing: MetaOapg.properties.ringing
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
        self, name: typing_extensions.Literal["ringing"]
    ) -> MetaOapg.properties.ringing:
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
                "ringing",
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
        self, name: typing_extensions.Literal["ringing"]
    ) -> MetaOapg.properties.ringing:
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
                "ringing",
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
            None,
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
    ) -> "CallCreatedEvent":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


from model.call_response import CallResponse
from model.member_response import MemberResponse
