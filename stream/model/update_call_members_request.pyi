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

class UpdateCallMembersRequest(
    schemas.DictBase, schemas.NoneBase, schemas.Schema, schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            class remove_members(schemas.ListSchema):
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
                ) -> "remove_members":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)

            class update_members(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["MemberRequest"]:
                        return MemberRequest
                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["MemberRequest"], typing.List["MemberRequest"]
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "update_members":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "MemberRequest":
                    return super().__getitem__(i)
            __annotations__ = {
                "remove_members": remove_members,
                "update_members": update_members,
            }
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["remove_members"]
    ) -> MetaOapg.properties.remove_members: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["update_members"]
    ) -> MetaOapg.properties.update_members: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "remove_members",
                "update_members",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["remove_members"]
    ) -> typing.Union[MetaOapg.properties.remove_members, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["update_members"]
    ) -> typing.Union[MetaOapg.properties.update_members, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "remove_members",
                "update_members",
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
        remove_members: typing.Union[
            MetaOapg.properties.remove_members, list, tuple, schemas.Unset
        ] = schemas.unset,
        update_members: typing.Union[
            MetaOapg.properties.update_members, list, tuple, schemas.Unset
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
    ) -> "UpdateCallMembersRequest":
        return super().__new__(
            cls,
            *_args,
            remove_members=remove_members,
            update_members=update_members,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.member_request import MemberRequest