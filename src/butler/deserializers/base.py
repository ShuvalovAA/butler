from collections.abc import Mapping

from ..types import Toml


def check_mapping(v: Toml):
    if isinstance(v, Mapping):
        return v
    raise TypeError


def check_str(v: Toml):
    if isinstance(v, str):
        return v
    raise TypeError
