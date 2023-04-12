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

class JoinCallRequest(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            create = schemas.BoolSchema

            @staticmethod
            def data() -> typing.Type["CallRequest"]:
                return CallRequest
            datacenter_hinted_id = schemas.StrSchema

            class members_limit(schemas.Int32Schema):
                pass
            ring = schemas.BoolSchema
            __annotations__ = {
                "create": create,
                "data": data,
                "datacenter_hinted_id": datacenter_hinted_id,
                "members_limit": members_limit,
                "ring": ring,
            }
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["create"]
    ) -> MetaOapg.properties.create: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> "CallRequest": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["datacenter_hinted_id"]
    ) -> MetaOapg.properties.datacenter_hinted_id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["members_limit"]
    ) -> MetaOapg.properties.members_limit: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["ring"]
    ) -> MetaOapg.properties.ring: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "create",
                "data",
                "datacenter_hinted_id",
                "members_limit",
                "ring",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["create"]
    ) -> typing.Union[MetaOapg.properties.create, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["data"]
    ) -> typing.Union["CallRequest", schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["datacenter_hinted_id"]
    ) -> typing.Union[MetaOapg.properties.datacenter_hinted_id, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["members_limit"]
    ) -> typing.Union[MetaOapg.properties.members_limit, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["ring"]
    ) -> typing.Union[MetaOapg.properties.ring, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "create",
                "data",
                "datacenter_hinted_id",
                "members_limit",
                "ring",
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
        create: typing.Union[
            MetaOapg.properties.create, bool, schemas.Unset
        ] = schemas.unset,
        data: typing.Union["CallRequest", schemas.Unset] = schemas.unset,
        datacenter_hinted_id: typing.Union[
            MetaOapg.properties.datacenter_hinted_id, str, schemas.Unset
        ] = schemas.unset,
        members_limit: typing.Union[
            MetaOapg.properties.members_limit, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        ring: typing.Union[
            MetaOapg.properties.ring, bool, schemas.Unset
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
    ) -> "JoinCallRequest":
        return super().__new__(
            cls,
            *_args,
            create=create,
            data=data,
            datacenter_hinted_id=datacenter_hinted_id,
            members_limit=members_limit,
            ring=ring,
            _configuration=_configuration,
            **kwargs,
        )

from stream.model.call_request import CallRequest
