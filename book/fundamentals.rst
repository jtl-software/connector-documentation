.. _fundamentals:

Fundamentals
============

The JTL-Connector request flow
------------------------------

JTL-Connector follows the same pattern for every request:

<Request diagram>

Incoming JSON requests are decoded and validated inside the :doc:`Core</glossary/core>`.
It decodes the RPC requests and identifies the RPC parameters as well as the RPC method which has to be called.

Each RPC method will be mapped to a controller method which will be then invoked.

In default implementation Application invoking controller method with RPC parameters as arguments.
Data returned from method is converted back into a RPC response and returned to the client.

.. note::
    The :doc:`Core</glossary/core>` handles requests by default but it can be also handled by the endpoint implementation.
    You can check more about it :ref:`here <request_handling>`.

To review:

- Each request executed by JTL-Wawi arrives the endpoint as RPC call, encoded as a JSON object
- The :doc:`Core</glossary/core>` decodes this request and determines the RPC parameters and RPC method
- The :doc:`Core</glossary/core>` or the endpoint maps the RPC method to its appropriate controller method and invokes it
- The controller method performs the request and returns a result which in turn will be passed to the :doc:`Core</glossary/core>`
- The :doc:`Core</glossary/core>` encodes this result as a valid RPC response and returns it to JTL-Wawi

Configuration
-------------

When instantiating the connector application, you can pass two optional arguments: config that implements ``Noodlehaus\ConfigInterface`` and ``Jtl\Connector\Core\Config\ConfigSchema`` class.

Let's focus on second one ``Jtl\Connector\Core\Config\ConfigSchema``. This class is used to define what parameters must/can contain config. In short it validates
config class. You can use default parameters or extend this by your own. You can read more about configuration later in this book.

Config class should implement ``Noodlehaus\ConfigInterface`` class interface. By default you can use ``Jtl\Connector\Core\Config\FileConfig``.

Core definitions classes
------------------------

Core contain special classes in ``Jtl\Connector\Core\Definition`` namespace. Definitions are describing connector environment in different parts.
Here is list with short description about them:

- Action
    - contain all action names that can be called. Can be used to check if action belongs to core or endpoint.
- Controller
    - contain controller names. Can be used to check if given name is real controller name
- ErrorCode.php
    - application error codes
- Event
    - can be used to generating event names see :doc:`events  </plugins/events>`
- IdentityType
    - contain identity types used by connector
- Model
    - contain model names and their mapping to identity
- PaymentType
    - contain payment types that are handled by JTL-Wawi
- RelationType
    - is responsible for defining relations between main identities and image identities
- RpcMethod
    - helper class for defining core rpc methods, contains also method mapping (redirection) to other methods
      for example connector.identify method will be mapped to core.connector.identify


A JTL-Connector request in action
---------------------------------

Suppose you want to handle the RPC method `product.push`.
This method is responsible for insert or update new product data into the online shop system.

First, start by creating a `Product` controller class in your endpoint.

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

All controller objects that handle `push` method must implement :code:`Jtl\Connector\Core\Controller\PushInterface`.
In order to handle another RPC actions controller must implement:

- :code:`Jtl\Connector\Core\Controller\PushInterface` for push
- :code:`Jtl\Connector\Core\Controller\PullInterface` for pull
- :code:`Jtl\Connector\Core\Controller\DeleteInterface` for delete
- :code:`Jtl\Connector\Core\Controller\StatisticsInterface` for statistics

There is also one more interface :code:`Jtl\Connector\Core\Controller\TransactionalInterface` that helps to handle
transactional way of making request. Methods from this interface will be called only on `push` and `delete` RPC calls.

Second example present usage of Delete and Transaction interface.

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
