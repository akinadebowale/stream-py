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


class WSClientEvent(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This is just a placeholder for all client events
    """

    class MetaOapg:
        class properties:
            connection_id = schemas.StrSchema
            __annotations__ = {
                "connection_id": connection_id,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["connection_id"]
    ) -> MetaOapg.properties.connection_id:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self, name: typing.Union[typing_extensions.Literal["connection_id",], str]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["connection_id"]
    ) -> typing.Union[MetaOapg.properties.connection_id, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self, name: typing.Union[typing_extensions.Literal["connection_id",], str]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        connection_id: typing.Union[
            MetaOapg.properties.connection_id, str, schemas.Unset
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
    ) -> "WSClientEvent":
        return super().__new__(
            cls,
            *_args,
            connection_id=connection_id,
            _configuration=_configuration,
            **kwargs,
        )
