Protocol basics
===============

JTL-Connector uses a protocol similar to JSON-RPC, along with some vendor-specific modifications.
To fully understand how an endpoint works, one needs at least a basic understanding of its function.

As stated earlier, JTL-Connector follows the MVC (Model-View-Controller) pattern.
The :doc:`jtlconnector </glossary/jtlconnector>` library provides both models and view logic.
JTL-Connector's view logic is represented by the layer that provides the RPC protocol implementation we are using.

The models are PHP versions of the domain objects inside JTL-Wawi.
They must stay compatible for JTL-Connector to work properly with JTL-Wawi.

RPC Protocol versioning
-----------------------

In the future data structure changes inside :doc:`jtlconnector </glossary/jtlconnector>` are likely to happen.
These modifications become necessary when new functionality is being introduced or existing functionality changes its behaviour in a way that breaks BC (backwards compatibility).
To detect incompatibilities between the version of JTL-Wawi and the models used by the running endpoint, the models carry a **protocol version** kept by :doc:`jtlconnector </glossary/jtlconnector>`.
JTL-Wawi verifies this protocol version and is thus able to detect when its own version number and the one communicated by the endpoint do not match.
In this case an error message appears in JTL-Wawi and the synchronization process is aborted.

.. note::
    :doc:`jtlconnector </glossary/jtlconnector>` is updated regularly.
    You can (and should) follow its development to be informed about updates that break BC.

.. _data-models:

Data models
-----------

All models used by JTL-Connector live inside the :code:`jtl\Connector\Model` namespace.
Refer to their source code to learn about the data they supply.
Each RPC call transports a hierarchy of data objects that belong together.

Some of these data objects have a special position throughout communication.
Those objects (called **main objects**) are not only data objects but are also used as RPC objects, i.e. they are being used in RPC calls.
The main objects are:

- Category
- Customer
- CustomerOrder
- DeliveryNote
- GlobalData
- Image
- Manufacturer
- Payment
- Product
- Specific

There are the following additional RPC objects that cover special functionality, although **they are not considered as main objects**:

- Connector
- ProductPrice
- ProductStockLevel
- StatusChange