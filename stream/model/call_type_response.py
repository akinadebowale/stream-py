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


class CallTypeResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "grants",
            "settings",
            "updated_at",
            "name",
            "created_at",
        }

        class properties:
            created_at = schemas.DateTimeSchema

            class grants(schemas.DictSchema):
                class MetaOapg:
                    class additional_properties(schemas.ListSchema):
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
                            _configuration: typing.Optional[
                                schemas.Configuration
                            ] = None,
                        ) -> "additional_properties":
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )

                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)

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
                        list,
                        tuple,
                    ],
                ) -> "grants":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            name = schemas.StrSchema

            @staticmethod
            def settings() -> typing.Type["CallSettingsResponse"]:
                return CallSettingsResponse

            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "created_at": created_at,
                "grants": grants,
                "name": name,
                "settings": settings,
                "updated_at": updated_at,
            }

    grants: MetaOapg.properties.grants
    settings: "CallSettingsResponse"
    updated_at: MetaOapg.properties.updated_at
    name: MetaOapg.properties.name
    created_at: MetaOapg.properties.created_at

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["grants"]
    ) -> MetaOapg.properties.grants:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["settings"]
    ) -> "CallSettingsResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "created_at",
                "grants",
                "name",
                "settings",
                "updated_at",
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
        self, name: typing_extensions.Literal["grants"]
    ) -> MetaOapg.properties.grants:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["settings"]
    ) -> "CallSettingsResponse":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["updated_at"]
    ) -> MetaOapg.properties.updated_at:
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
                "grants",
                "name",
                "settings",
                "updated_at",
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
        grants: typing.Union[
            MetaOapg.properties.grants,
            dict,
            frozendict.frozendict,
        ],
        settings: "CallSettingsResponse",
        updated_at: typing.Union[
            MetaOapg.properties.updated_at,
            str,
            datetime,
        ],
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
        created_at: typing.Union[
            MetaOapg.properties.created_at,
            str,
            datetime,
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
    ) -> "CallTypeResponse":
        return super().__new__(
            cls,
            *_args,
            grants=grants,
            settings=settings,
            updated_at=updated_at,
            name=name,
            created_at=created_at,
            _configuration=_configuration,
            **kwargs,
        )


from stream.model.call_settings_response import CallSettingsResponse
