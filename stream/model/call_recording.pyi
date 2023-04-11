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

class CallRecording(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "start_time",
            "filename",
            "end_time",
            "url",
        }

        class properties:
            end_time = schemas.DateTimeSchema
            filename = schemas.StrSchema
            start_time = schemas.DateTimeSchema
            url = schemas.StrSchema
            __annotations__ = {
                "end_time": end_time,
                "filename": filename,
                "start_time": start_time,
                "url": url,
            }
    start_time: MetaOapg.properties.start_time
    filename: MetaOapg.properties.filename
    end_time: MetaOapg.properties.end_time
    url: MetaOapg.properties.url

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["end_time"]
    ) -> MetaOapg.properties.end_time: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["filename"]
    ) -> MetaOapg.properties.filename: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["start_time"]
    ) -> MetaOapg.properties.start_time: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["url"]
    ) -> MetaOapg.properties.url: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "end_time",
                "filename",
                "start_time",
                "url",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["end_time"]
    ) -> MetaOapg.properties.end_time: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["filename"]
    ) -> MetaOapg.properties.filename: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["start_time"]
    ) -> MetaOapg.properties.start_time: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["url"]
    ) -> MetaOapg.properties.url: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "end_time",
                "filename",
                "start_time",
                "url",
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
        start_time: typing.Union[
            MetaOapg.properties.start_time,
            str,
            datetime,
        ],
        filename: typing.Union[
            MetaOapg.properties.filename,
            str,
        ],
        end_time: typing.Union[
            MetaOapg.properties.end_time,
            str,
            datetime,
        ],
        url: typing.Union[
            MetaOapg.properties.url,
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
    ) -> "CallRecording":
        return super().__new__(
            cls,
            *_args,
            start_time=start_time,
            filename=filename,
            end_time=end_time,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )
