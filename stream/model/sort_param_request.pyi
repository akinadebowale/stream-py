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

class SortParamRequest(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            direction = schemas.Int32Schema
            field = schemas.StrSchema
            __annotations__ = {
                "direction": direction,
                "field": field,
            }
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["direction"]
    ) -> MetaOapg.properties.direction: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["field"]
    ) -> MetaOapg.properties.field: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "direction",
                "field",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["direction"]
    ) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["field"]
    ) -> typing.Union[MetaOapg.properties.field, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "direction",
                "field",
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
        direction: typing.Union[
            MetaOapg.properties.direction, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        field: typing.Union[
            MetaOapg.properties.field, str, schemas.Unset
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
    ) -> "SortParamRequest":
        return super().__new__(
            cls,
            *_args,
            direction=direction,
            field=field,
            _configuration=_configuration,
            **kwargs,
        )
