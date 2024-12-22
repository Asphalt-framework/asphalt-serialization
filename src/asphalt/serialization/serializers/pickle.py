from __future__ import annotations

import pickle
from typing import Any

from .._api import Serializer
from .._exceptions import DeserializationError, SerializationError


class PickleSerializer(Serializer):
    """
    Serializes objects using the standard library :mod:`pickle` module.

    .. warning:: This serializer is insecure because it allows execution of arbitrary
        code when deserializing. Avoid using this if at all possible.

    :param protocol: pickle protocol level to use (defaults to the highest possible)
    """

    __slots__ = "protocol"

    def __init__(self, protocol: int = pickle.HIGHEST_PROTOCOL):
        assert (
            0 <= protocol <= pickle.HIGHEST_PROTOCOL
        ), f'"protocol" must be between 0 and {pickle.HIGHEST_PROTOCOL}'

        self.protocol: int = protocol

    def serialize(self, obj: Any) -> bytes:
        try:
            return pickle.dumps(obj, protocol=self.protocol)
        except Exception as exc:
            raise SerializationError(str(exc)) from exc

    def deserialize(self, payload: bytes) -> Any:
        try:
            return pickle.loads(payload)
        except Exception as exc:
            raise DeserializationError(str(exc)) from exc

    @property
    def mimetype(self) -> str:
        return "application/python-pickle"
