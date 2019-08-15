.. _primary-key-mapper:

Primary key mapper
==================

A key component in every endpoint is the **primary key mapper**.
This special class translates between JTL-Wawi's information and the shop's database.
It identifies each object by its *database primary key* (PK) and stores mapping information that represent the relation between JTL-Wawi's PK (called **host ID**) and the PK used in the shop (called **endpoint ID**).

All primary key mapper classes implement the interface `jtl\\Connector\\Mapper\\IPrimaryKeyMapper <https://github.com/jtl-software/connector/blob/2.6/src/Mapper/IPrimaryKeyMapper.php>`_.
This interface enforces simple CRUD operations on all available mappings.
It is up to the endpoint to decide how these mappings are stored providing that they are somehow persistent.

The example endpoint uses its SQLite3 database to store all primary key mappings, implementing the class is therefore pretty straightforward.
