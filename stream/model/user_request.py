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

from stream.model import schemas  # noqa: F401


class UserRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "id",
        }

        class properties:
            id = schemas.StrSchema

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

            image = schemas.StrSchema
            name = schemas.StrSchema
            role = schemas.StrSchema

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
                "id": id,
                "custom": custom,
                "image": image,
                "name": name,
                "role": role,
                "teams": teams,
            }

    id: MetaOapg.properties.id

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["custom"]
    ) -> MetaOapg.properties.custom:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["image"]
    ) -> MetaOapg.properties.image:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["role"]
    ) -> MetaOapg.properties.role:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["teams"]
    ) -> MetaOapg.properties.teams:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "id",
                "custom",
                "image",
                "name",
                "role",
                "teams",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["custom"]
    ) -> typing.Union[MetaOapg.properties.custom, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["image"]
    ) -> typing.Union[MetaOapg.properties.image, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> typing.Union[MetaOapg.properties.name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["role"]
    ) -> typing.Union[MetaOapg.properties.role, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["teams"]
    ) -> typing.Union[MetaOapg.properties.teams, schemas.Unset]:
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
                "id",
                "custom",
                "image",
                "name",
                "role",
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
        id: typing.Union[
            MetaOapg.properties.id,
            str,
        ],
        custom: typing.Union[
            MetaOapg.properties.custom, dict, frozendict.frozendict, schemas.Unset
        ] = schemas.unset,
        image: typing.Union[
            MetaOapg.properties.image, str, schemas.Unset
        ] = schemas.unset,
        name: typing.Union[
            MetaOapg.properties.name, str, schemas.Unset
        ] = schemas.unset,
        role: typing.Union[
            MetaOapg.properties.role, str, schemas.Unset
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
    ) -> "UserRequest":
        return super().__new__(
            cls,
            *_args,
            id=id,
            custom=custom,
            image=image,
            name=name,
            role=role,
            teams=teams,
            _configuration=_configuration,
            **kwargs,
        )
