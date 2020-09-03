.. _fundamentals:

Fundamentals
============

The JTL-Connector request flow
------------------------------

JTL-Connector follows the same pattern for every request:

<Request diagram>

Incoming JSON requests are decoded and validated inside the :doc:`jtlconnector </glossary/jtlconnector>` library.
:doc:`jtlconnector </glossary/jtlconnector>` decodes the RPC requests and identifies the RPC object and its method to be called.

Each RPC object maps to a controller object inside the endpoint whose respective method will then be invoked.
The RPC method :code:`product.push` thus maps to an invocation of the controller method :code:`Product::push()`.
Application handles routing by default but it can also be handled by endpoint.

Each controller method that is invoked receives the RPC parameters as method arguments.
The controller method performs the actual request and returns a certain result.
This result is then being wrapped inside an RPC response and returned to the client.

To review:

- Each request executed by JTL-Wawi arrives as an RPC call, encoded as a JSON object
- The :doc:`jtlconnector </glossary/jtlconnector>` library decodes this request and determines RPC object and method
- It passes this information along with the RPC parameters to the endpoint (optional)
- The endpoint maps RPC object and method to its appropriate controller and method and invokes it (optional)
- The controller method performs the request and returns a result which in turn will be passed to :doc:`jtlconnector </glossary/jtlconnector>`
- :doc:`jtlconnector </glossary/jtlconnector>` encodes this result as a valid RPC response and returns it to JTL-Wawi

Configuration
-------------

When creating Application class you can pass two optional arguments: config that implements ``Noodlehaus\ConfigInterface`` and ``Jtl\Connector\Core\Config\ConfigSchema`` class.

Let's focus on second one ``Jtl\Connector\Core\Config\ConfigSchema``. This class is used to define what parameters must/can contain config. In short it validates
config class. You can use default parameters or extend this by your own.

Config class should implement ``Noodlehaus\ConfigInterface`` class interface. By default you can use ``Jtl\Connector\Core\Config\FileConfig``.

Core definitions classes
------------------------

New core contain special classes in ``Jtl\Connector\Core\Definition`` namespace. Definitions are describing connector environment in different parts.
Here are

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
