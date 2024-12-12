import pytest
from asphalt.core import Context

from asphalt.serialization.api import CustomizableSerializer, Serializer
from asphalt.serialization.component import SerializationComponent
from asphalt.serialization.serializers.json import JSONSerializer
from asphalt.serialization.serializers.msgpack import MsgpackSerializer
from asphalt.serialization.serializers.pickle import PickleSerializer


@pytest.mark.asyncio
async def test_customizable_serializer() -> None:
    component = SerializationComponent(backend="json")
    async with Context() as ctx:
        await component.start(ctx)

        resource = ctx.get_resource_nowait(Serializer)
        assert isinstance(resource, JSONSerializer)

        resource2 = ctx.get_resource_nowait(CustomizableSerializer)
        assert resource2 is resource

        resource3 = ctx.get_resource_nowait(JSONSerializer)
        assert resource3 is resource


@pytest.mark.asyncio
async def test_non_customizable_serializer() -> None:
    component = SerializationComponent(backend="pickle")
    async with Context() as ctx:
        await component.start(ctx)

        resource = ctx.get_resource_nowait(Serializer)
        assert isinstance(resource, PickleSerializer)

        assert not ctx.get_resource_nowait(CustomizableSerializer, optional=True)

        resource2 = ctx.get_resource_nowait(PickleSerializer)
        assert resource2 is resource


@pytest.mark.asyncio
async def test_resource_name() -> None:
    component = SerializationComponent(backend="msgpack", resource_name="alternate")
    async with Context() as ctx:
        await component.start(ctx)

        resource = ctx.get_resource_nowait(Serializer, "alternate")
        assert isinstance(resource, MsgpackSerializer)

        resource2 = ctx.get_resource_nowait(CustomizableSerializer, "alternate")
        assert resource2 is resource

        resource3 = ctx.get_resource_nowait(MsgpackSerializer, "alternate")
        assert resource3 is resource
