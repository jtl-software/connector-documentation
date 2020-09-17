.. _fundamentals:

Fundamentals
============

.. _architecture:

Architecture
------------

The interface between :doc:`JTL-Wawi </glossary/jtl-wawi>` and :doc:`JTL-Connector </glossary/jtl-connector>` consists of two layers.
The first layer - provided by JTL-Software - is called :doc:`Core</glossary/core>`.

.. image:: /_images/connector_flow.png

The :doc:`Core</glossary/core>` arbitrates between :doc:`JTL-Wawi </glossary/jtl-wawi>` and your so-called **endpoint** logic.
Your endpoint is the last piece of code and bridges between the :doc:`Core</glossary/core>` and your target system.

To achieve this JTL-Connector makes use of the widely known MVC pattern.
The :doc:`Core</glossary/core>` provides the models and the view layer.
Your opportunity is to provide the appropriate controller code to read data from or write data to your target system.


Request flow
------------

Incoming JSON requests are decoded and validated inside the :doc:`Core</glossary/core>`.
It decodes the RPC requests and identifies the RPC parameters as well as the RPC method which has to be called.

Each RPC method will be mapped to a controller method which will be then invoked.

In the default implementation, the :doc:`Core</glossary/core>` application is invoking a controller method with RPC parameters as arguments.
The parameters are getting processed by the controller method and the result is returned to the application.
In the last step the result will be converted into a RPC response and sent back to the client.

.. note::
    The :doc:`Core</glossary/core>` handles requests by default but it can be also handled by the endpoint implementation.
    You can check more about it :ref:`here <request_handling>`.

To review:

- Each call - executed by JTL-Wawi - arrives the endpoint as RPC request.
- The :doc:`Core</glossary/core>` decodes this request and determines the RPC parameters and RPC method.
- The :doc:`Core</glossary/core>` or the endpoint maps the RPC method to its appropriate controller method and invokes it.
- The controller method performs the request and returns a result which in turn will be passed to the :doc:`Core</glossary/core>`.
- The :doc:`Core</glossary/core>` encodes this result as a valid RPC response and sends it back to JTL-Wawi.

Configuration
-------------

Two optional arguments can be passed when the connector :doc:`Application</book/application>` is getting instantiated:

- ``$config`` - an object which implements the ``Noodlehaus\ConfigInterface`` interface
- ``$configSchema`` - an object which extends the ``Jtl\Connector\Core\Config\ConfigSchema`` class

Let's focus on the class of the second argument, the ``Jtl\Connector\Core\Config\ConfigSchema``. It is used to define which parameters must or may exist in the configuration. In short it validates
the connector configuration. You can just use the default parameters required by the Core or add more parameters by your own. You can read more about this in the chapter :doc:`configuration</book/configuration>`.

The used configuration class must implement the ``Noodlehaus\ConfigInterface`` interface. By default an instance of ``Jtl\Connector\Core\Config\FileConfig`` is used.

Core definitions
----------------

The Core contains special classes in the ``Jtl\Connector\Core\Definition`` namespace. Definitions are describing the connector environment in different parts.
Here is a short description about them:

+-------------+---------------------------------------------------------------------------------------------------------+
|Name         |Description                                                                                              |
+=============+=========================================================================================================+
|Action       |Contains all action names that can be called. Can be used to check if action belongs to core or endpoint.|
+-------------+---------------------------------------------------------------------------------------------------------+
|Controller   |Contains controller names. Can be used to check if given name is real controller name.                   |
+-------------+---------------------------------------------------------------------------------------------------------+
|ErrorCode    |Application error codes.                                                                                 |
+-------------+---------------------------------------------------------------------------------------------------------+
|Event        |Can be used to generate event names (see :doc:`events  </plugins/events>`).                              |
+-------------+---------------------------------------------------------------------------------------------------------+
|IdentityType |Contains identity types used by connector.                                                               |
+-------------+---------------------------------------------------------------------------------------------------------+
|Model        |Contains model names and their mapping to identities.                                                    |
+-------------+---------------------------------------------------------------------------------------------------------+
|PaymentType  |Contains payment types that are known by JTL-Wawi.                                                       |
+-------------+---------------------------------------------------------------------------------------------------------+
|RelationType |Is responsible for defining relations between main identities and image identities.                      |
+-------------+---------------------------------------------------------------------------------------------------------+
|RpcMethod    |Helper class for defining RPC methods. Contains also method mappings (redirection) to other methods.     |
|             |The method ``connector.identify`` method will be mapped to ``core.connector.identify`` for example.      |
+-------------+---------------------------------------------------------------------------------------------------------+


Request in action
-----------------

Suppose you want to handle the RPC method `product.push`.
This method is responsible for insert or update new product data into the online shop system.

We start with creating a `Product` controller class in the endpoint implementation.

.. code-block:: php

    // src/Controller/Product.php
    namespace Acme\Connector\AcmeShop\Controller;

    use Jtl\Connector\Core\Controller;
    use Jtl\Connector\Core\Model\AbstractDataModel;

    class Product implements PushInterface
    {
        public function push(AbstractDataModel $model) : AbstractDataModel;
        {
            return $model;
        }
    }

All controller objects that handle a `push` method must implement the ``Jtl\Connector\Core\Controller\PushInterface`` interface.
In order to handle other RPC actions, the controller must implement:

- ``Jtl\Connector\Core\Controller\PushInterface`` for push
- ``Jtl\Connector\Core\Controller\PullInterface`` for pull
- ``Jtl\Connector\Core\Controller\DeleteInterface`` for delete
- ``Jtl\Connector\Core\Controller\StatisticsInterface`` for statistics

There is one more interface which helps to handle requests inside a transaction, the ``Jtl\Connector\Core\Controller\TransactionalInterface`` interface.
Methods from this interface will be called only on `push` and `delete` RPC calls.

The second example shows the implementation of the TransactionalInterface in a controller which also implements a `delete` action.

.. code-block:: php

    namespace Acme\Connector\AcmeShop\Controller;

    use Jtl\Connector\Core\Controller;
    use Jtl\Connector\Core\Model\AbstractDataModel;

    class Product implements DeleteInterface, TransactionalInterface
    {
        public function delete(AbstractDataModel $model) : AbstractDataModel;
        {
            return $model;
        }

        public function beginTransaction(): bool
        {
            // called before 'delete' method
        }

        public function commit(): bool
        {
            // called after 'delete' method
        }

        public function rollback(): bool;
        {
            // called when exception was thrown in 'delete' method
        }
    }
