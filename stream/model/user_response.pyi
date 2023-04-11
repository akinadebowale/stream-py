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

class UserResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "role",
            "updated_at",
            "custom",
            "created_at",
            "id",
        }

        class properties:
            created_at = schemas.DateTimeSchema

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
            role = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            deleted_at = schemas.DateTimeSchema
            image = schemas.StrSchema
            name = schemas.StrSchema

            class teams(schemas.ListSchema):
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
                ) -> "teams":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "created_at": created_at,
                "custom": custom,
                "id": id,
                "role": role,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "image": image,
                "name": name,
                "teams": teams,
            }
    role: MetaOapg.properties.role
    updated_at: MetaOapg.properties.updated_at
    custom: MetaOapg.properties.custom
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["role"]
    ) -> MetaOapg.properties.role: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["deleted_at"]
    ) -> MetaOapg.properties.deleted_at: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["image"]
    ) -> MetaOapg.properties.image: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["teams"]
    ) -> MetaOapg.properties.teams: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "custom",
                "id",
                "role",
                "updated_at",
                "deleted_at",
                "image",
                "name",
                "teams",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["role"]
    ) -> MetaOapg.properties.role: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["deleted_at"]
    ) -> typing.Union[MetaOapg.properties.deleted_at, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["image"]
    ) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["teams"]
    ) -> typing.Union[MetaOapg.properties.teams, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "custom",
                "id",
                "role",
                "updated_at",
                "deleted_at",
                "image",
                "name",
                "teams",
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
        role: typing.Union[
            MetaOapg.properties.role,
            str,
        ],
        updated_at: typing.Union[
            MetaOapg.properties.updated_at,
            str,
            datetime,
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
        id: typing.Union[
            MetaOapg.properties.id,
            str,
        ],
        deleted_at: typing.Union[
            MetaOapg.properties.deleted_at, str, datetime, schemas.Unset
        ] = schemas.unset,
        image: typing.Union[
            MetaOapg.properties.image, str, schemas.Unset
        ] = schemas.unset,
        name: typing.Union[
            MetaOapg.properties.name, str, schemas.Unset
        ] = schemas.unset,
        teams: typing.Union[
            MetaOapg.properties.teams, list, tuple, schemas.Unset
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
    ) -> "UserResponse":
        return super().__new__(
            cls,
            *_args,
            role=role,
            updated_at=updated_at,
            custom=custom,
            created_at=created_at,
            id=id,
            deleted_at=deleted_at,
            image=image,
            name=name,
            teams=teams,
            _configuration=_configuration,
            **kwargs,
        )
