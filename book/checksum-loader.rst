Checksum loader
===============

Many shop systems (endpoints) have the ability to work with product variation combinations.
Usually, due to its complex data structure, this is one of the most heavyweight and resource intensive tasks.
To avoid unnecessary database queries and/or file operations, and to guarantee optimal performance the JTL-Connector uses an object of the interface ``Jtl\Connector\Core\Checksum\ChecksumLoaderInterface``.

It provides methods to write, read and delete checksums based on an endpoint id and its corresponding data type (for now we only use it for products).

When a new product is pushed to the endpoint, its checksum (based on variation data) gets saved by the checksum loader.
If the same product is pushed/updated again, the previously saved checksum is loaded and will be checked for differences.
If the checksum is still the same, it means there were no differences in the products variations so that the corresponding code and queries for this data can be skipped.

.. note::
    As the checksum loader is optional, you are not forced to use it. In case you decide that its not necessary or does not have any important impact on the connector performance,
    you are free to skip the implementation. However, you should carefully make sure that this is reasonable.
