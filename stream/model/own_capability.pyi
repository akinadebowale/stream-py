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

class OwnCapability(schemas.EnumBase, schemas.StrSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    All possibility of string to use
    """

    @schemas.classproperty
    def BLOCKUSERS(cls):
        return cls("block-users")
    @schemas.classproperty
    def CREATECALL(cls):
        return cls("create-call")
    @schemas.classproperty
    def CREATEREACTION(cls):
        return cls("create-reaction")
    @schemas.classproperty
    def ENDCALL(cls):
        return cls("end-call")
    @schemas.classproperty
    def JOINBACKSTAGE(cls):
        return cls("join-backstage")
    @schemas.classproperty
    def JOINCALL(cls):
        return cls("join-call")
    @schemas.classproperty
    def JOINENDEDCALL(cls):
        return cls("join-ended-call")
    @schemas.classproperty
    def MUTEUSERS(cls):
        return cls("mute-users")
    @schemas.classproperty
    def READCALL(cls):
        return cls("read-call")
    @schemas.classproperty
    def REMOVECALLMEMBER(cls):
        return cls("remove-call-member")
    @schemas.classproperty
    def SCREENSHARE(cls):
        return cls("screenshare")
    @schemas.classproperty
    def SENDAUDIO(cls):
        return cls("send-audio")
    @schemas.classproperty
    def SENDVIDEO(cls):
        return cls("send-video")
    @schemas.classproperty
    def STARTBROADCASTCALL(cls):
        return cls("start-broadcast-call")
    @schemas.classproperty
    def STARTRECORDCALL(cls):
        return cls("start-record-call")
    @schemas.classproperty
    def STARTTRANSCRIPTIONCALL(cls):
        return cls("start-transcription-call")
    @schemas.classproperty
    def STOPBROADCASTCALL(cls):
        return cls("stop-broadcast-call")
    @schemas.classproperty
    def STOPRECORDCALL(cls):
        return cls("stop-record-call")
    @schemas.classproperty
    def STOPTRANSCRIPTIONCALL(cls):
        return cls("stop-transcription-call")
    @schemas.classproperty
    def UPDATECALL(cls):
        return cls("update-call")
    @schemas.classproperty
    def UPDATECALLMEMBER(cls):
        return cls("update-call-member")
    @schemas.classproperty
    def UPDATECALLPERMISSIONS(cls):
        return cls("update-call-permissions")
    @schemas.classproperty
    def UPDATECALLSETTINGS(cls):
        return cls("update-call-settings")
