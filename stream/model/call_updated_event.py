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


class CallUpdatedEvent(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
        Ref: https://openapi-generator.tech

        Do not edit the class manually.

        This event is sent when a call is updated, clients should use this update the local state of the call.
    This event also contains the capabilities by role for the call, clients should update the own_capability for the current.
    """

    class MetaOapg:
        required = {
            "call",
            "call_cid",
            "created_at",
            "capabilities_by_role",
            "type",
        }

        class properties:
            @staticmethod
            def call() -> typing.Type["CallResponse"]:
                return CallResponse

            call_cid = schemas.StrSchema

            class capabilities_by_role(schemas.DictSchema):
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
                ) -> "capabilities_by_role":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            created_at = schemas.DateTimeSchema
            type = schemas.StrSchema
            __annotations__ = {
                "call": call,
                "call_cid": call_cid,
                "capabilities_by_role": capabilities_by_role,
                "created_at": created_at,
                "type": type,
            }

    call: "CallResponse"
    call_cid: MetaOapg.properties.call_cid
    created_at: MetaOapg.properties.created_at
    capabilities_by_role: MetaOapg.properties.capabilities_by_role
    type: MetaOapg.properties.type

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["call"]) -> "CallResponse":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["capabilities_by_role"]
    ) -> MetaOapg.properties.capabilities_by_role:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call",
                "call_cid",
                "capabilities_by_role",
                "created_at",
                "type",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["call"]) -> "CallResponse":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["capabilities_by_role"]
    ) -> MetaOapg.properties.capabilities_by_role:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type:
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
                "call",
                "call_cid",
                "capabilities_by_role",
                "created_at",
                "type",
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
    ) -> "CallUpdatedEvent":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


from stream.model.call_response import CallResponse
