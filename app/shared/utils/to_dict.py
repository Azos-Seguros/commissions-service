from dataclasses import asdict, is_dataclass

from pydantic import BaseModel


def to_dict(data):
    if is_dataclass(data):
        return asdict(data)
    elif isinstance(data, dict):
        return data
    elif isinstance(data, BaseModel):
        return data.model_dump(by_alias=True)
    else:
        raise TypeError("Expected dict or dataclass")
