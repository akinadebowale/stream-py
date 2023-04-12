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

from stream.model import schemas  # noqa: F401


class Device(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "user_id",
            "push_provider",
            "created_at",
            "id",
        }

        class properties:
            created_at = schemas.DateTimeSchema
            id = schemas.StrSchema
            push_provider = schemas.StrSchema
            user_id = schemas.StrSchema
            disabled = schemas.BoolSchema
            disabled_reason = schemas.StrSchema
            push_provider_name = schemas.StrSchema
            __annotations__ = {
                "created_at": created_at,
                "id": id,
                "push_provider": push_provider,
                "user_id": user_id,
                "disabled": disabled,
                "disabled_reason": disabled_reason,
                "push_provider_name": push_provider_name,
            }

    user_id: MetaOapg.properties.user_id
    push_provider: MetaOapg.properties.push_provider
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["push_provider"]
    ) -> MetaOapg.properties.push_provider:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["user_id"]
    ) -> MetaOapg.properties.user_id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["disabled"]
    ) -> MetaOapg.properties.disabled:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["disabled_reason"]
    ) -> MetaOapg.properties.disabled_reason:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["push_provider_name"]
    ) -> MetaOapg.properties.push_provider_name:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "id",
                "push_provider",
                "user_id",
                "disabled",
                "disabled_reason",
                "push_provider_name",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["push_provider"]
    ) -> MetaOapg.properties.push_provider:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["user_id"]
    ) -> MetaOapg.properties.user_id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["disabled"]
    ) -> typing.Union[MetaOapg.properties.disabled, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["disabled_reason"]
    ) -> typing.Union[MetaOapg.properties.disabled_reason, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["push_provider_name"]
    ) -> typing.Union[MetaOapg.properties.push_provider_name, schemas.Unset]:
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
                "created_at",
                "id",
                "push_provider",
                "user_id",
                "disabled",
                "disabled_reason",
                "push_provider_name",
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
        disabled: typing.Union[
            MetaOapg.properties.disabled, bool, schemas.Unset
        ] = schemas.unset,
        disabled_reason: typing.Union[
            MetaOapg.properties.disabled_reason, str, schemas.Unset
        ] = schemas.unset,
        push_provider_name: typing.Union[
            MetaOapg.properties.push_provider_name, str, schemas.Unset
        ] = schemas.unset,
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
    ) -> "Device":
        return super().__new__(
            cls,
            *_args,
            disabled=disabled,
            disabled_reason=disabled_reason,
            push_provider_name=push_provider_name,
            _configuration=_configuration,
            **kwargs,
        )
