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

class ScreensharingSettings(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "access_request_enabled",
            "enabled",
        }

        class properties:
            access_request_enabled = schemas.BoolSchema
            enabled = schemas.BoolSchema
            __annotations__ = {
                "access_request_enabled": access_request_enabled,
                "enabled": enabled,
            }
    access_request_enabled: MetaOapg.properties.access_request_enabled
    enabled: MetaOapg.properties.enabled

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["access_request_enabled"]
    ) -> MetaOapg.properties.access_request_enabled: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["enabled"]
    ) -> MetaOapg.properties.enabled: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "access_request_enabled",
                "enabled",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["access_request_enabled"]
    ) -> MetaOapg.properties.access_request_enabled: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["enabled"]
    ) -> MetaOapg.properties.enabled: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "access_request_enabled",
                "enabled",
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
        access_request_enabled: typing.Union[
            MetaOapg.properties.access_request_enabled,
            bool,
        ],
        enabled: typing.Union[
            MetaOapg.properties.enabled,
            bool,
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
    ) -> "ScreensharingSettings":
        return super().__new__(
            cls,
            *_args,
            access_request_enabled=access_request_enabled,
            enabled=enabled,
            _configuration=_configuration,
            **kwargs,
        )
