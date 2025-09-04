from dataclasses import asdict, is_dataclass


def to_dict(data):
    if is_dataclass(data):
        return asdict(data)
    elif isinstance(data, dict):
        return data
    else:
        raise TypeError("Expected dict or dataclass")
