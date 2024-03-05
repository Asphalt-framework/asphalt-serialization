"""An example that demonstrates how to serialize custom types."""

# isort: off
from __future__ import annotations

from dataclasses import dataclass

import anyio
from asphalt.core import CLIApplicationComponent, run_application, require_resource
from asphalt.serialization import CustomizableSerializer


@dataclass
class Book:
    name: str
    author: str
    year: int
    isbn: str
    sequel: Book | None = None


class ApplicationComponent(CLIApplicationComponent):
    async def start(self) -> None:
        self.add_component("serialization", backend="json")
        await super().start()

    async def run(self) -> int | None:
        serializer = require_resource(CustomizableSerializer)
        serializer.register_custom_type(Book, typename="Book")  # typename is optional
        book2 = Book("The Fall of Hyperion", "Dan Simmons", 1995, "978-0553288209")
        book1 = Book("Hyperion", "Dan Simmons", 1989, "978-0553283686", book2)
        payload = serializer.serialize(book1)
        print("JSON serialized dict:", payload.decode())
        return None


anyio.run(run_application, ApplicationComponent())
