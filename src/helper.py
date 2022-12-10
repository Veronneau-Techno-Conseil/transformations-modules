from typing import Any, Callable


def dict_or_none(dct: dict[str, Any], field: str):
    if field in dct.keys:
        return dct[field]
    return None


def dict_del_or_none(dct: dict[str, Any], field: str, action: Callable[[Any], Any]):
    if field in dct:
        return action(dct[field])
    return None
