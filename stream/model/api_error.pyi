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

class APIError(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "duration",
            "code",
            "more_info",
            "details",
            "message",
            "StatusCode",
        }

        class properties:
            StatusCode = schemas.Int32Schema
            code = schemas.Int32Schema

            class details(schemas.ListSchema):
                class MetaOapg:
                    items = schemas.IntSchema
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                MetaOapg.items,
                                decimal.Decimal,
                                int,
                            ]
                        ],
                        typing.List[
                            typing.Union[
                                MetaOapg.items,
                                decimal.Decimal,
                                int,
                            ]
                        ],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "details":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            duration = schemas.StrSchema
            message = schemas.StrSchema
            more_info = schemas.StrSchema

            class exception_fields(schemas.DictSchema):
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                def __getitem__(
                    self, name: typing.Union[str,]
                ) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                def get_item_oapg(
                    self, name: typing.Union[str,]
                ) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
                def __new__(
                    cls,
                    *_args: typing.Union[
                        dict,
                        frozendict.frozendict,
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[
                        MetaOapg.additional_properties,
                        str,
                    ],
                ) -> "exception_fields":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "StatusCode": StatusCode,
                "code": code,
                "details": details,
                "duration": duration,
                "message": message,
                "more_info": more_info,
                "exception_fields": exception_fields,
            }
    duration: MetaOapg.properties.duration
    code: MetaOapg.properties.code
    more_info: MetaOapg.properties.more_info
    details: MetaOapg.properties.details
    message: MetaOapg.properties.message
    StatusCode: MetaOapg.properties.StatusCode

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["StatusCode"]
    ) -> MetaOapg.properties.StatusCode: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["code"]
    ) -> MetaOapg.properties.code: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["details"]
    ) -> MetaOapg.properties.details: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["message"]
    ) -> MetaOapg.properties.message: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["more_info"]
    ) -> MetaOapg.properties.more_info: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["exception_fields"]
    ) -> MetaOapg.properties.exception_fields: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "StatusCode",
                "code",
                "details",
                "duration",
                "message",
                "more_info",
                "exception_fields",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["StatusCode"]
    ) -> MetaOapg.properties.StatusCode: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["code"]
    ) -> MetaOapg.properties.code: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["details"]
    ) -> MetaOapg.properties.details: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["message"]
    ) -> MetaOapg.properties.message: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["more_info"]
    ) -> MetaOapg.properties.more_info: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["exception_fields"]
    ) -> typing.Union[MetaOapg.properties.exception_fields, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "StatusCode",
                "code",
                "details",
                "duration",
                "message",
                "more_info",
                "exception_fields",
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
        exception_fields: typing.Union[
            MetaOapg.properties.exception_fields,
            dict,
            frozendict.frozendict,
            schemas.Unset,
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
    ) -> "APIError":
        return super().__new__(
            cls,
            *_args,
            exception_fields=exception_fields,
            _configuration=_configuration,
            **kwargs,
        )
