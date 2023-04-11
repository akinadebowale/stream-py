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

class Coordinates(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "latitude",
            "longitude",
        }

        class properties:
            latitude = schemas.Float32Schema
            longitude = schemas.Float32Schema
            __annotations__ = {
                "latitude": latitude,
                "longitude": longitude,
            }
    latitude: MetaOapg.properties.latitude
    longitude: MetaOapg.properties.longitude

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["latitude"]
    ) -> MetaOapg.properties.latitude: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["longitude"]
    ) -> MetaOapg.properties.longitude: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "latitude",
                "longitude",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["latitude"]
    ) -> MetaOapg.properties.latitude: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["longitude"]
    ) -> MetaOapg.properties.longitude: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "latitude",
                "longitude",
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
        latitude: typing.Union[
            MetaOapg.properties.latitude,
            decimal.Decimal,
            int,
            float,
        ],
        longitude: typing.Union[
            MetaOapg.properties.longitude,
            decimal.Decimal,
            int,
            float,
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
    ) -> "Coordinates":
        return super().__new__(
            cls,
            *_args,
            latitude=latitude,
            longitude=longitude,
            _configuration=_configuration,
            **kwargs,
        )
