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

class GetOrCreateCallResponse(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "call",
            "duration",
            "created",
            "members",
            "blocked_users",
        }

        class properties:
            class blocked_users(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["UserResponse"]:
                        return UserResponse
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["UserResponse"], typing.List["UserResponse"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "blocked_users":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "UserResponse":
                    return super().__getitem__(i)
            @staticmethod
            def call() -> typing.Type["CallResponse"]:
                return CallResponse
            created = schemas.BoolSchema
            duration = schemas.StrSchema

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
            @staticmethod
            def membership() -> typing.Type["MemberResponse"]:
                return MemberResponse
            __annotations__ = {
                "blocked_users": blocked_users,
                "call": call,
                "created": created,
                "duration": duration,
                "members": members,
                "membership": membership,
            }
    call: "CallResponse"
    duration: MetaOapg.properties.duration
    created: MetaOapg.properties.created
    members: MetaOapg.properties.members
    blocked_users: MetaOapg.properties.blocked_users

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["blocked_users"]
    ) -> MetaOapg.properties.blocked_users: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["call"]
    ) -> "CallResponse": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created"]
    ) -> MetaOapg.properties.created: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["members"]
    ) -> MetaOapg.properties.members: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["membership"]
    ) -> "MemberResponse": ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "blocked_users",
                "call",
                "created",
                "duration",
                "members",
                "membership",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["blocked_users"]
    ) -> MetaOapg.properties.blocked_users: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["call"]
    ) -> "CallResponse": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created"]
    ) -> MetaOapg.properties.created: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["members"]
    ) -> MetaOapg.properties.members: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["membership"]
    ) -> typing.Union["MemberResponse", schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "blocked_users",
                "call",
                "created",
                "duration",
                "members",
                "membership",
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
        membership: typing.Union["MemberResponse", schemas.Unset] = schemas.unset,
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
    ) -> "GetOrCreateCallResponse":
        return super().__new__(
            cls,
            *_args,
            membership=membership,
            _configuration=_configuration,
            **kwargs,
        )

from stream.model.call_response import CallResponse
from stream.model.member_response import MemberResponse
from stream.model.user_response import UserResponse
