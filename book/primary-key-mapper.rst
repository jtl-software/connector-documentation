.. _primary-key-mapper:

Primary key mapper
==================

A key component of an endpoint implementation is the :ref:`primary key mapper<primary-key-mapper-class>` class.
It translates between JTL-Wawi and the shop by storing the unique properties of all objects.
A single set of properties represents the relation of an object between JTL-Wawi (called **host ID**) and the shop (called **endpoint ID**).

.. note::
    The **host ID** is the primary key of the object in JTL-Wawi.

.. note::
    In most cases the **endpoint ID** is the primary key of the object in the shop.

All primary key mapper classes must implement the `Jtl\\Connector\\Core\\Mapper\\PrimaryKeyMapperInterface <https://github.com/jtl-software/core/blob/develop/src/Mapper/PrimaryKeyMapperInterface.php>`_ interface.
This interface enforces simple CRUD operations on all available mappings.
It is up to the endpoint implementation to decide how these mappings are stored, providing that they are somehow persistent.
