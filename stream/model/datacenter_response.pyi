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

class DatacenterResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "latency_url",
            "coordinates",
            "name",
        }

        class properties:
            @staticmethod
            def coordinates() -> typing.Type["Coordinates"]:
                return Coordinates
            latency_url = schemas.StrSchema
            name = schemas.StrSchema
            __annotations__ = {
                "coordinates": coordinates,
                "latency_url": latency_url,
                "name": name,
            }
    latency_url: MetaOapg.properties.latency_url
    coordinates: "Coordinates"
    name: MetaOapg.properties.name

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["coordinates"]
    ) -> "Coordinates": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["latency_url"]
    ) -> MetaOapg.properties.latency_url: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "coordinates",
                "latency_url",
                "name",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["coordinates"]
    ) -> "Coordinates": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["latency_url"]
    ) -> MetaOapg.properties.latency_url: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "coordinates",
                "latency_url",
                "name",
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
        latency_url: typing.Union[
            MetaOapg.properties.latency_url,
            str,
        ],
        coordinates: "Coordinates",
        name: typing.Union[
            MetaOapg.properties.name,
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
    ) -> "DatacenterResponse":
        return super().__new__(
            cls,
            *_args,
            latency_url=latency_url,
            coordinates=coordinates,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from model.coordinates import Coordinates
