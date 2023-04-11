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

class CallReactionEvent(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This event is sent when a reaction is sent in a call, clients should use this to show the reaction in the call screen
    """

    class MetaOapg:
        required = {
            "reaction",
            "call_cid",
            "created_at",
            "type",
        }

        class properties:
            call_cid = schemas.StrSchema
            created_at = schemas.DateTimeSchema

            @staticmethod
            def reaction() -> typing.Type["ReactionResponse"]:
                return ReactionResponse
            type = schemas.StrSchema
            __annotations__ = {
                "call_cid": call_cid,
                "created_at": created_at,
                "reaction": reaction,
                "type": type,
            }
    reaction: "ReactionResponse"
    call_cid: MetaOapg.properties.call_cid
    created_at: MetaOapg.properties.created_at
    type: MetaOapg.properties.type

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["reaction"]
    ) -> "ReactionResponse": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call_cid",
                "created_at",
                "reaction",
                "type",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["call_cid"]
    ) -> MetaOapg.properties.call_cid: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["created_at"]
    ) -> MetaOapg.properties.created_at: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["reaction"]
    ) -> "ReactionResponse": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["type"]
    ) -> MetaOapg.properties.type: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "call_cid",
                "created_at",
                "reaction",
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
    ) -> "CallReactionEvent":
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.reaction_response import ReactionResponse
