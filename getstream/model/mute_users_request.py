# coding: utf-8

"""
    Stream Video API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v80.4.1
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

from getstream.model import schemas  # noqa: F401


class MuteUsersRequest(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            audio = schemas.BoolSchema
            mute_all_users = schemas.BoolSchema
            screenshare = schemas.BoolSchema

            class user_ids(schemas.ListSchema):
                class MetaOapg:
                    items = schemas.StrSchema

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                MetaOapg.items,
                                str,
                            ]
                        ],
                        typing.List[
                            typing.Union[
                                MetaOapg.items,
                                str,
                            ]
                        ],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "user_ids":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            video = schemas.BoolSchema
            __annotations__ = {
                "audio": audio,
                "mute_all_users": mute_all_users,
                "screenshare": screenshare,
                "user_ids": user_ids,
                "video": video,
            }

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["audio"]
    ) -> MetaOapg.properties.audio:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["mute_all_users"]
    ) -> MetaOapg.properties.mute_all_users:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["screenshare"]
    ) -> MetaOapg.properties.screenshare:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["user_ids"]
    ) -> MetaOapg.properties.user_ids:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["video"]
    ) -> MetaOapg.properties.video:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "audio",
                "mute_all_users",
                "screenshare",
                "user_ids",
                "video",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["audio"]
    ) -> typing.Union[MetaOapg.properties.audio, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["mute_all_users"]
    ) -> typing.Union[MetaOapg.properties.mute_all_users, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["screenshare"]
    ) -> typing.Union[MetaOapg.properties.screenshare, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["user_ids"]
    ) -> typing.Union[MetaOapg.properties.user_ids, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["video"]
    ) -> typing.Union[MetaOapg.properties.video, schemas.Unset]:
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
                "audio",
                "mute_all_users",
                "screenshare",
                "user_ids",
                "video",
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
        audio: typing.Union[
            MetaOapg.properties.audio, bool, schemas.Unset
        ] = schemas.unset,
        mute_all_users: typing.Union[
            MetaOapg.properties.mute_all_users, bool, schemas.Unset
        ] = schemas.unset,
        screenshare: typing.Union[
            MetaOapg.properties.screenshare, bool, schemas.Unset
        ] = schemas.unset,
        user_ids: typing.Union[
            MetaOapg.properties.user_ids, list, tuple, schemas.Unset
        ] = schemas.unset,
        video: typing.Union[
            MetaOapg.properties.video, bool, schemas.Unset
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
    ) -> "MuteUsersRequest":
        return super().__new__(
            cls,
            *_args,
            audio=audio,
            mute_all_users=mute_all_users,
            screenshare=screenshare,
            user_ids=user_ids,
            video=video,
            _configuration=_configuration,
            **kwargs,
        )