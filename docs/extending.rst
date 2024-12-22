Writing new serializer backends
===============================

.. py:currentmodule:: asphalt.serialization

If you wish to implement an alternate method of serialization, you can do so by
subclassing the :class:`~Serializer` class. There are three methods implementors must
override:

* :meth:`~Serializer.serialize`
* :meth:`~Serializer.deserialize`
* :meth:`~Serializer.mimetype`

The ``mimetype`` method is a ``@property`` that simply returns the MIME type appropriate
for the serialization scheme. This property is used by certain other components. If you
cannot find an applicable MIME type, you can use ``application/octet-stream``.

.. note:: Serializers must always serialize to bytes; never serialize to strings!

If you want your serializer to be available as a backend for
:class:`~asphalt.serialization.SerializationComponent`, you need to add the
corresponding entry point for it. Suppose your serializer class is named
``AwesomeSerializer``, lives in the package ``foo.bar.awesome`` and you want to give it
the alias ``awesome``, add this line to your project's ``pyproject.toml`` under the
``entry_points`` argument in the ``asphalt.serialization.serializers`` namespace:

.. code-block:: toml

    [project.entry-points."asphalt.serialization.serializers"]
    awesome = "foo.bar.awesome:AwesomeSerializer"
