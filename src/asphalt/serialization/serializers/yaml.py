from __future__ import annotations

from io import StringIO
from typing import Any

from ruamel.yaml import YAML

from .. import DeserializationError, SerializationError
from .._api import Serializer


class YAMLSerializer(Serializer):
    """
    Serializes objects to and from YAML format.

    To use this serializer backend, the ``ruamel.yaml`` library must be installed.
    A convenient way to do this is to install ``asphalt-serialization`` with the
    ``yaml`` extra:

    .. code-block:: shell

        $ pip install asphalt-serialization[yaml]

    .. warning:: This serializer is insecure in unsafe mode because it allows execution
      of arbitrary code when deserializing.

    .. seealso:: `ruamel.yaml documentation <https://yaml.readthedocs.io/en/latest/>`_
    """

    def __init__(self) -> None:
        self._yaml = YAML()

    def serialize(self, obj: Any) -> bytes:
        try:
            buffer = StringIO()
            self._yaml.dump(obj, buffer)
            return buffer.getvalue().encode("utf-8")
        except Exception as exc:
            raise SerializationError(str(exc)) from exc

    def deserialize(self, payload: bytes) -> Any:
        try:
            return self._yaml.load(payload)
        except Exception as exc:
            raise DeserializationError(str(exc)) from exc

    @property
    def mimetype(self) -> str:
        return "text/yaml"

    @property
    def safe(self) -> bool:
        """Returns ``True`` if the safe mode is being used with (de)serialization."""
        return "safe" in self._yaml.typ
