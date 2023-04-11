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

from openapi_client import schemas  # noqa: F401


class StopLiveResponse(
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
        }

        class properties:
            @staticmethod
            def call() -> typing.Type["CallResponse"]:
                return CallResponse

            duration = schemas.StrSchema
            __annotations__ = {
                "call": call,
                "duration": duration,
            }

    call: "CallResponse"
    duration: MetaOapg.properties.duration

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["call"]) -> "CallResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call",
                "duration",
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
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration:
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
                "duration",
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
    ) -> "StopLiveResponse":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


from openapi_client.model.call_response import CallResponse
