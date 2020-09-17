Checksum loader
===============

Many shop systems have the ability to work with product variation combinations.
In some systems is updating the product variations one of the most heavyweight and resource intensive tasks.
To avoid unnecessary database queries and/or file operations, and to guarantee optimal performance, the endpoint can make use of an object of a class that implements the ``Jtl\Connector\Core\Checksum\ChecksumLoaderInterface`` interface.

It provides methods to write, read and delete checksums based on an endpoint id and its corresponding data type (for now we only use it for products).

When a new product is pushed to the endpoint, its checksum (based on variation data) is getting saved by the checksum loader.
If the same product is pushed/updated again, the previously saved checksum is loaded and will be checked for differences.
If the checksum did not change, means the variations related data of the product did not change, so updating the variations in the shop can be skipped.

.. note::
    Using the checksum loader is optional. In case you decide it is not necessary or it does not have any important impact on the connector performance, you are free to skip the implementation.
