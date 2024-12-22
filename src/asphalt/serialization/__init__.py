from ._api import CustomizableSerializer as CustomizableSerializer
from ._api import CustomTypeCodec as CustomTypeCodec
from ._api import Serializer as Serializer
from ._component import SerializationComponent as SerializationComponent
from ._exceptions import DeserializationError as DeserializationError
from ._exceptions import SerializationError as SerializationError
from ._marshalling import default_marshaller as default_marshaller
from ._marshalling import default_unmarshaller as default_unmarshaller
from ._object_codec import DefaultCustomTypeCodec as DefaultCustomTypeCodec

# Re-export imports, so they look like they live directly in this package
for __value in list(locals().values()):
    if getattr(__value, "__module__", "").startswith(f"{__name__}."):
        __value.__module__ = __name__

del __value
