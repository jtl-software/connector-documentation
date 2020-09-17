RPC Protocol
============

JTL-Connector uses a protocol similar to JSON-RPC, along with some vendor-specific modifications.
To fully understand how an endpoint works, at least a basic understanding of its function is required.

As stated earlier, JTL-Connector follows the MVC (Model-View-Controller) pattern.
The :doc:`Core</glossary/core>` library provides both models and view logic.
JTL-Connector's view logic is represented by the layer that provides the RPC protocol implementation we are using.

The models are PHP versions of the domain objects inside JTL-Wawi.
They must stay compatible for JTL-Connector to work properly with JTL-Wawi.

Protocol versioning
-------------------

Data structure changes inside :doc:`Core</glossary/core>` are likely to happen in future.
These modifications become necessary when new functionality is being introduced or existing functionality changes its behaviour in a way that breaks backwards compatibility (BC).
To detect incompatibilities between the version of JTL-Wawi and the models used by the running endpoint, a supported **protocol version** is set by the :doc:`Core</glossary/core>`.
The protocol version sent by the endpoint is verified from JTL-Wawi. An error message appears in JTL-Wawi and the synchronization process is aborted in case the versions do not match.

.. note::
    The :doc:`Core</glossary/core>` is updated regularly.
    You can (and should) follow its development, to be informed about updates that break BC.

.. _data-models:

Data models
-----------

All models used by JTL-Connector stay inside the :code:`Jtl\Connector\Core\Model` namespace.
Refer to their source code to learn about the data they supply.
Each RPC call transports a hierarchy of data objects that belong together.

Some of these data objects have a special position throughout communication.
Those objects (called **main objects**) are not only data objects, they are also used as RPC objects, i.e. they are being used in RPC calls.
The main objects are:

- Category
- Customer
- CustomerOrder
- CrossSelling
- DeliveryNote
- GlobalData
- Image
- Manufacturer
- Payment
- Product
- Specific

The following additional RPC objects cover special functionality, although **they are not considered as main objects**:

- Connector
- ProductPrice
- ProductStockLevel
- StatusChange