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


class MemberResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "updated_at",
            "user_id",
            "custom",
            "created_at",
            "user",
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

            updated_at = schemas.DateTimeSchema

            @staticmethod
            def user() -> typing.Type["UserResponse"]:
                return UserResponse

            user_id = schemas.StrSchema
            deleted_at = schemas.DateTimeSchema
            role = schemas.StrSchema
            __annotations__ = {
                "created_at": created_at,
                "custom": custom,
                "updated_at": updated_at,
                "user": user,
                "user_id": user_id,
                "deleted_at": deleted_at,
                "role": role,
            }

    updated_at: MetaOapg.properties.updated_at
    user_id: MetaOapg.properties.user_id
    custom: MetaOapg.properties.custom
    created_at: MetaOapg.properties.created_at
    user: "UserResponse"

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> "UserResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["user_id"]
    ) -> MetaOapg.properties.user_id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["deleted_at"]
    ) -> MetaOapg.properties.deleted_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["role"]
    ) -> MetaOapg.properties.role:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "custom",
                "updated_at",
                "user",
                "user_id",
                "deleted_at",
                "role",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at:
        ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> "UserResponse":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["user_id"]
    ) -> MetaOapg.properties.user_id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["deleted_at"]
    ) -> typing.Union[MetaOapg.properties.deleted_at, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["role"]
    ) -> typing.Union[MetaOapg.properties.role, schemas.Unset]:
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
                "created_at",
                "custom",
                "updated_at",
                "user",
                "user_id",
                "deleted_at",
                "role",
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
        updated_at: typing.Union[
            MetaOapg.properties.updated_at,
            str,
            datetime,
        ],
        user_id: typing.Union[
            MetaOapg.properties.user_id,
            str,
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
        user: "UserResponse",
        deleted_at: typing.Union[
            MetaOapg.properties.deleted_at, str, datetime, schemas.Unset
        ] = schemas.unset,
        role: typing.Union[
            MetaOapg.properties.role, str, schemas.Unset
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
    ) -> "MemberResponse":
        return super().__new__(
            cls,
            *_args,
            updated_at=updated_at,
            user_id=user_id,
            custom=custom,
            created_at=created_at,
            user=user,
            deleted_at=deleted_at,
            role=role,
            _configuration=_configuration,
            **kwargs,
        )


from stream.model.user_response import UserResponse
