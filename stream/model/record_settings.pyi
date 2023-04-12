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

class RecordSettings(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "mode",
            "audio_only",
            "quality",
        }

        class properties:
            audio_only = schemas.BoolSchema

            class mode(schemas.EnumBase, schemas.StrSchema):
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("available")
                @schemas.classproperty
                def DISABLED(cls):
                    return cls("disabled")
                @schemas.classproperty
                def AUTOON(cls):
                    return cls("auto-on")

            class quality(schemas.EnumBase, schemas.StrSchema):
                @schemas.classproperty
                def AUDIOONLY(cls):
                    return cls("audio-only")
                @schemas.classproperty
                def DIGIT_THREE_60P(cls):
                    return cls("360p")
                @schemas.classproperty
                def DIGIT_FOUR_80P(cls):
                    return cls("480p")
                @schemas.classproperty
                def DIGIT_SEVEN_20P(cls):
                    return cls("720p")
                @schemas.classproperty
                def DIGIT_ONE_080P(cls):
                    return cls("1080p")
                @schemas.classproperty
                def DIGIT_ONE_440P(cls):
                    return cls("1440p")
            __annotations__ = {
                "audio_only": audio_only,
                "mode": mode,
                "quality": quality,
            }
    mode: MetaOapg.properties.mode
    audio_only: MetaOapg.properties.audio_only
    quality: MetaOapg.properties.quality

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["audio_only"]
    ) -> MetaOapg.properties.audio_only: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["mode"]
    ) -> MetaOapg.properties.mode: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["quality"]
    ) -> MetaOapg.properties.quality: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "audio_only",
                "mode",
                "quality",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["audio_only"]
    ) -> MetaOapg.properties.audio_only: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["mode"]
    ) -> MetaOapg.properties.mode: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["quality"]
    ) -> MetaOapg.properties.quality: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "audio_only",
                "mode",
                "quality",
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
        mode: typing.Union[
            MetaOapg.properties.mode,
            str,
        ],
        audio_only: typing.Union[
            MetaOapg.properties.audio_only,
            bool,
        ],
        quality: typing.Union[
            MetaOapg.properties.quality,
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
    ) -> "RecordSettings":
        return super().__new__(
            cls,
            *_args,
            mode=mode,
            audio_only=audio_only,
            quality=quality,
            _configuration=_configuration,
            **kwargs,
        )
