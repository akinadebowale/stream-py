# THIS FILE IS GENERATED FROM github.com/GetStream/protocol/tree/main/openapi-gen/templates/python/type.tmpl
from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class TargetResolution:
    height: int = field(metadata=config(field_name="height"))
    width: int = field(metadata=config(field_name="width"))
    bitrate: int = field(metadata=config(field_name="bitrate"))
