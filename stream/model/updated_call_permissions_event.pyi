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

class UpdatedCallPermissionsEvent(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This event is sent to notify about permission changes for a user, clients receiving this event should update their UI accordingly
    """

    class MetaOapg:
        required = {
            "own_capabilities",
            "call_cid",
            "created_at",
            "type",
            "user",
        }

        class properties:
            call_cid = schemas.StrSchema
            created_at = schemas.DateTimeSchema

            class own_capabilities(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["OwnCapability"]:
                        return OwnCapability
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["OwnCapability"], typing.List["OwnCapability"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "own_capabilities":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "OwnCapability":
                    return super().__getitem__(i)
            type = schemas.StrSchema

            @staticmethod
            def user() -> typing.Type["UserResponse"]:
                return UserResponse
            __annotations__ = {
                "call_cid": call_cid,
                "created_at": created_at,
                "own_capabilities": own_capabilities,
                "type": type,
                "user": user,
            }
    own_capabilities: MetaOapg.properties.own_capabilities
    call_cid: MetaOapg.properties.call_cid
    created_at: MetaOapg.properties.created_at
    type: MetaOapg.properties.type
    user: "UserResponse"

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["own_capabilities"]
    ) -> MetaOapg.properties.own_capabilities: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["user"]
    ) -> "UserResponse": ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call_cid",
                "created_at",
                "own_capabilities",
                "type",
                "user",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["own_capabilities"]
    ) -> MetaOapg.properties.own_capabilities: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["user"]
    ) -> "UserResponse": ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call_cid",
                "created_at",
                "own_capabilities",
                "type",
                "user",
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
    ) -> "UpdatedCallPermissionsEvent":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from stream.model.own_capability import OwnCapability
from stream.model.user_response import UserResponse
