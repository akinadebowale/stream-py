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


class CallResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Represents a call
    """

    class MetaOapg:
        required = {
            "settings",
            "blocked_user_ids",
            "custom",
            "created_at",
            "recording",
            "type",
            "created_by",
            "broadcasting",
            "own_capabilities",
            "transcribing",
            "updated_at",
            "backstage",
            "id",
            "cid",
        }

        class properties:
            backstage = schemas.BoolSchema

            class blocked_user_ids(schemas.ListSchema):
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
                ) -> "blocked_user_ids":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            broadcasting = schemas.BoolSchema
            cid = schemas.StrSchema
            created_at = schemas.DateTimeSchema

            @staticmethod
            def created_by() -> typing.Type["UserResponse"]:
                return UserResponse

            class custom(schemas.DictSchema):
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema

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
                        dict,
                        frozendict.frozendict,
                        str,
                        date,
                        datetime,
                        uuid.UUID,
                        int,
                        float,
                        decimal.Decimal,
                        bool,
                        None,
                        list,
                        tuple,
                        bytes,
                        io.FileIO,
                        io.BufferedReader,
                    ],
                ) -> "custom":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            id = schemas.StrSchema

            class own_capabilities(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["OwnCapability"]:
                        return OwnCapability

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["OwnCapability"], typing.List["OwnCapability"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "own_capabilities":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> "OwnCapability":
                    return super().__getitem__(i)

            recording = schemas.BoolSchema

            @staticmethod
            def settings() -> typing.Type["CallSettingsResponse"]:
                return CallSettingsResponse

            transcribing = schemas.BoolSchema
            type = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            ended_at = schemas.DateTimeSchema
            starts_at = schemas.DateTimeSchema
            team = schemas.StrSchema
            __annotations__ = {
                "backstage": backstage,
                "blocked_user_ids": blocked_user_ids,
                "broadcasting": broadcasting,
                "cid": cid,
                "created_at": created_at,
                "created_by": created_by,
                "custom": custom,
                "id": id,
                "own_capabilities": own_capabilities,
                "recording": recording,
                "settings": settings,
                "transcribing": transcribing,
                "type": type,
                "updated_at": updated_at,
                "ended_at": ended_at,
                "starts_at": starts_at,
                "team": team,
            }

    settings: "CallSettingsResponse"
    blocked_user_ids: MetaOapg.properties.blocked_user_ids
    custom: MetaOapg.properties.custom
    created_at: MetaOapg.properties.created_at
    recording: MetaOapg.properties.recording
    type: MetaOapg.properties.type
    created_by: "UserResponse"
    broadcasting: MetaOapg.properties.broadcasting
    own_capabilities: MetaOapg.properties.own_capabilities
    transcribing: MetaOapg.properties.transcribing
    updated_at: MetaOapg.properties.updated_at
    backstage: MetaOapg.properties.backstage
    id: MetaOapg.properties.id
    cid: MetaOapg.properties.cid

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["backstage"]
    ) -> MetaOapg.properties.backstage:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["blocked_user_ids"]
    ) -> MetaOapg.properties.blocked_user_ids:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["broadcasting"]
    ) -> MetaOapg.properties.broadcasting:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["cid"]
    ) -> MetaOapg.properties.cid:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_by"]
    ) -> "UserResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["own_capabilities"]
    ) -> MetaOapg.properties.own_capabilities:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["recording"]
    ) -> MetaOapg.properties.recording:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["settings"]
    ) -> "CallSettingsResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["transcribing"]
    ) -> MetaOapg.properties.transcribing:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["ended_at"]
    ) -> MetaOapg.properties.ended_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["starts_at"]
    ) -> MetaOapg.properties.starts_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["team"]
    ) -> MetaOapg.properties.team:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "backstage",
                "blocked_user_ids",
                "broadcasting",
                "cid",
                "created_at",
                "created_by",
                "custom",
                "id",
                "own_capabilities",
                "recording",
                "settings",
                "transcribing",
                "type",
                "updated_at",
                "ended_at",
                "starts_at",
                "team",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["backstage"]
    ) -> MetaOapg.properties.backstage:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["blocked_user_ids"]
    ) -> MetaOapg.properties.blocked_user_ids:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["broadcasting"]
    ) -> MetaOapg.properties.broadcasting:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["cid"]
    ) -> MetaOapg.properties.cid:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_by"]
    ) -> "UserResponse":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["own_capabilities"]
    ) -> MetaOapg.properties.own_capabilities:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["recording"]
    ) -> MetaOapg.properties.recording:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["settings"]
    ) -> "CallSettingsResponse":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["transcribing"]
    ) -> MetaOapg.properties.transcribing:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["ended_at"]
    ) -> typing.Union[MetaOapg.properties.ended_at, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["starts_at"]
    ) -> typing.Union[MetaOapg.properties.starts_at, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["team"]
    ) -> typing.Union[MetaOapg.properties.team, schemas.Unset]:
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
                "backstage",
                "blocked_user_ids",
                "broadcasting",
                "cid",
                "created_at",
                "created_by",
                "custom",
                "id",
                "own_capabilities",
                "recording",
                "settings",
                "transcribing",
                "type",
                "updated_at",
                "ended_at",
                "starts_at",
                "team",
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
        settings: "CallSettingsResponse",
        blocked_user_ids: typing.Union[
            MetaOapg.properties.blocked_user_ids,
            list,
            tuple,
        ],
        custom: typing.Union[
            MetaOapg.properties.custom,
            dict,
            frozendict.frozendict,
        ],
        created_at: typing.Union[
            MetaOapg.properties.created_at,
            str,
            datetime,
        ],
        recording: typing.Union[
            MetaOapg.properties.recording,
            bool,
        ],
        type: typing.Union[
            MetaOapg.properties.type,
            str,
        ],
        created_by: "UserResponse",
        broadcasting: typing.Union[
            MetaOapg.properties.broadcasting,
            bool,
        ],
        own_capabilities: typing.Union[
            MetaOapg.properties.own_capabilities,
            list,
            tuple,
        ],
        transcribing: typing.Union[
            MetaOapg.properties.transcribing,
            bool,
        ],
        updated_at: typing.Union[
            MetaOapg.properties.updated_at,
            str,
            datetime,
        ],
        backstage: typing.Union[
            MetaOapg.properties.backstage,
            bool,
        ],
        id: typing.Union[
            MetaOapg.properties.id,
            str,
        ],
        cid: typing.Union[
            MetaOapg.properties.cid,
            str,
        ],
        ended_at: typing.Union[
            MetaOapg.properties.ended_at, str, datetime, schemas.Unset
        ] = schemas.unset,
        starts_at: typing.Union[
            MetaOapg.properties.starts_at, str, datetime, schemas.Unset
        ] = schemas.unset,
        team: typing.Union[
            MetaOapg.properties.team, str, schemas.Unset
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
    ) -> "CallResponse":
        return super().__new__(
            cls,
            *_args,
            settings=settings,
            blocked_user_ids=blocked_user_ids,
            custom=custom,
            created_at=created_at,
            recording=recording,
            type=type,
            created_by=created_by,
            broadcasting=broadcasting,
            own_capabilities=own_capabilities,
            transcribing=transcribing,
            updated_at=updated_at,
            backstage=backstage,
            id=id,
            cid=cid,
            ended_at=ended_at,
            starts_at=starts_at,
            team=team,
            _configuration=_configuration,
            **kwargs,
        )


from model.call_settings_response import CallSettingsResponse
from model.own_capability import OwnCapability
from model.user_response import UserResponse
