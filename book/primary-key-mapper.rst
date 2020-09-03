.. _primary-key-mapper:

Primary key mapper
==================

A key component in every endpoint is the :ref:`primary key mapper<primary-key-mapper-class>` class.
This special class translates between JTL-Wawi's information and the shop's database.
It identifies each object by its unique properties and stores them. A single set of properties represents the relation of an object between JTL-Wawi (called **host ID**) and the unique properties in the shop (called **endpoint ID**).

.. note::
    The **host ID** is the primary key of the object in JTL-Wawi.

    In most cases the **endpoint ID** is the primary key of the object in the shop.

All primary key mapper classes implement the interface `Jtl\\Connector\\Core\\Mapper\\PrimaryKeyMapperInterface <https://github.com/jtl-software/connector-core/blob/develop/src/Mapper/PrimaryKeyMapperInterface.php>`_.
This interface enforces simple CRUD operations on all available mappings.
It is up to the endpoint implementation to decide how these mappings are stored providing that they are somehow persistent.
