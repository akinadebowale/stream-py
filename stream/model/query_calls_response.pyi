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

class QueryCallsResponse(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "duration",
            "calls",
        }

        class properties:
            class calls(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["CallStateResponseFields"]:
                        return CallStateResponseFields
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["CallStateResponseFields"],
                        typing.List["CallStateResponseFields"],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "calls":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "CallStateResponseFields":
                    return super().__getitem__(i)
            duration = schemas.StrSchema
            next = schemas.StrSchema
            prev = schemas.StrSchema
            __annotations__ = {
                "calls": calls,
                "duration": duration,
                "next": next,
                "prev": prev,
            }
    duration: MetaOapg.properties.duration
    calls: MetaOapg.properties.calls

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["calls"]
    ) -> MetaOapg.properties.calls: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["next"]
    ) -> MetaOapg.properties.next: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["prev"]
    ) -> MetaOapg.properties.prev: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "calls",
                "duration",
                "next",
                "prev",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["calls"]
    ) -> MetaOapg.properties.calls: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["next"]
    ) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["prev"]
    ) -> typing.Union[MetaOapg.properties.prev, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "calls",
                "duration",
                "next",
                "prev",
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
        next: typing.Union[
            MetaOapg.properties.next, str, schemas.Unset
        ] = schemas.unset,
        prev: typing.Union[
            MetaOapg.properties.prev, str, schemas.Unset
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
    ) -> "QueryCallsResponse":
        return super().__new__(
            cls,
            *_args,
            next=next,
            prev=prev,
            _configuration=_configuration,
            **kwargs,
        )

from stream.model.call_state_response_fields import CallStateResponseFields
