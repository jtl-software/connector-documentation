Fundamentals
============

The JTL-Connector request flow
------------------------------

JTL-Connector follows the same pattern for every request:

<Request diagram>

Incoming JSON requests are decoded and validated inside the :doc:`jtlconnector </glossary/jtlconnector>` library.
:doc:`jtlconnector </glossary/jtlconnector>` decodes the RPC requests and identifies the RPC object and its method to be called.

Each RPC object maps to a controller object inside the endpoint whose respective method will then be invoked.
The RPC method `product.push` thus maps to an invocation of the controller method Product::push().
It is the endpoint's responsibility to perform the actual routing.

Each controller method that is invoked receives the RPC parameters as method arguments.
The controller method performs the actual request and returns a certain result.
This result is then being wrapped inside an RPC response and returned to the client.

To review:

- Each request executed by JTL-Wawi arrives as an RPC call, encoded as a JSON object
- The :doc:`jtlconnector </glossary/jtlconnector>` library decodes this request and determines RPC object and method
- It passes this information along with the RPC parameters to the endpoint
- The endpoint maps RPC object and method to its appropriate controller and method and invokes it, passing the RPC parameters as arguments
- The controller method performs the request and returns a result which in turn will be passed to :doc:`jtlconnector </glossary/jtlconnector>`
- :doc:`jtlconnector </glossary/jtlconnector>` encodes this result as a valid RPC response and returns it to JTL-Wawi

A JTL-Connector request in action
---------------------------------

Suppose you want to handle the RPC method `product.push`.
This method is responsible for insert or update new product data into the online shop system.

First, start by creating a `Product` controller class in your endpoint.

.. code-block:: php

    // src/
