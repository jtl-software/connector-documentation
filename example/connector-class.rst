Connector class
===============

JTL-Connector makes use of an RPC-style communication protocol together with JTL-Wawi.
To write a full-featured endpoint implementation you do not have to know any detail on how this has been implemented.
At the moment it is enough to say that this protocol provides method call semantics to your endpoint, i.e. you provide methods, grouped into several RPC objects, that can be called from the client.
Those methods, of course, can have parameters.

All details of the communication, protocol decoding and verifications are abstracted away by :doc:`jtlconnector </glossary/jtlconnector>`.
The main hub for all requests is the **Connector** class whose job it is to check whether a certain RPC call can be handled by your endpoint or not.
Some RPC methods require a special treatment when being handled but most of them can be implemented pretty straightforward.

The (abridged) implementation of our example endpoint looks like this:

.. code-block:: php

    namespace jtl\Connector\Example;

    use jtl\Connector\Base\Connector as BaseConnector;
    use jtl\Connector\Core\Rpc\Method;
    use jtl\Connector\Core\Rpc\RequestPacket;
    use jtl\Connector\Core\Utilities\RpcMethod;
    use jtl\Connector\Core\Controller\Controller as CoreController;
    use jtl\Connector\Example\Authentication\TokenLoader;
    use jtl\Connector\Example\Checksum\ChecksumLoader;
    use jtl\Connector\Example\Mapper\PrimaryKeyMapper;
    use jtl\Connector\Result\Action;

    /**
     * Example Connector
     *
     * @access public
     */
    class Connector extends BaseConnector
    {
        protected $controller;
        protected $action;

        public function initialize()
        {
            $this->setPrimaryKeyMapper(new PrimaryKeyMapper())
                ->setTokenLoader(new TokenLoader())
                ->setChecksumLoader(new ChecksumLoader());
        }

        public function canHandle()
        {
            $controller = RpcMethod::buildController($this->getMethod()->getController());

            $class = "\\jtl\\Connector\\Example\\Controller\\{$controller}";
            if (class_exists($class)) {
                $this->controller = $class::getInstance();
                $this->action = RpcMethod::buildAction($this->getMethod()->getAction());

                return is_callable(array($this->controller, $this->action));
            }

            return false;
        }

        public function handle(RequestPacket $requestpacket)
        {
            $config = $this->getConfig();

            // Set the config to our controller
            $this->controller->setConfig($config);

            // Set the method to our controller
            $this->controller->setMethod($this->getMethod());

            if ($this->action === Method::ACTION_PUSH || $this->action === Method::ACTION_DELETE) {
                if (!is_array($requestpacket->getParams())) {
                    throw new \Exception("Expecting request array, invalid data given");
                }

                $action = new Action();
                $results = array();
                if ($this->action === Method::ACTION_PUSH && $this->getMethod()->getController() === 'product_price') {
                    $params = $requestpacket->getParams();
                    $result = $this->controller->update($params);
                    $results[] = $result->getResult();
                }
                else {
                    foreach ($requestpacket->getParams() as $param) {
                        $result = $this->controller->{$this->action}($param);
                        $results[] = $result->getResult();
                    }
                }

                $action->setHandled(true)
                    ->setResult($results)
                    ->setError($result->getError());

                return $action;
            }
            else {
                return $this->controller->{$this->action}($requestpacket->getParams());
            }
        }
    }

The `Connector` class extends from an abstract base implementation provided by :doc:`jtlconnector </glossary/jtlconnector>`.
It ensures that the `initialize` method is called exactly once for each HTTP request being made.
Inside this method three classes are being registered in the base connector class: the :doc:`PrimaryKeyMapper <primary-key-mapper>`, the :doc:`TokenLoader <token-loader>` and the :doc:`ChecksumLoader <checksum-loader>`.
We will explain them later.

`canHandle()` and `handle()`
----------------------------

For now, have a look at the `canHandle()` and `handle()` methods.
The `canHandle()` method checks whether a certain RPC method can be handled by this endpoint.
JTL-Connector has to do this check because different software products support different feature sets and JTL-Wawi needs to know whether the platform supports a certain feature or not.
The implementation above makes use of `Reflection <http://www.php.net/reflection>`_ to check whether the method is supported or not.

This rather simple, yet flexible approach translates e.g. the RPC method call `product.push` into the method `jtl\\Connector\\Example\\Controller\\Product::push()` which is then being called.

.. note::
    Your endpoint has to return true for each RPC method call it wants to receive.
    JTL-Connector additionally has more fine-grained means of informing JTL-Wawi about the target platforms abilities which are discussed later.

The `handle()` method actually performs the RPC call and invokes the appropriate controller method inside your code.
It basically boils down to taking the method parameters from the `$requestpacket` object and passing them to your controller.

Method types
------------

JTL-Connector has four important methods available on almost all of the defined RPC objects, **push**, **pull**, **delete** and **statistic**.

**push** receives data from the client to be stored in the target system and can be imagined as a combined insert/update call.

**pull** loads an object from the target system.

**delete** tries to delete an object from the target system in a fault-tolerant way.

**statistic** provides the number of new objects that have not yet been pulled by the client.

.. note::
    For details on how *new* objects can be distinguished from the remaining ones, see the :doc:`PrimaryKeyMapper <primary-key-mapper>` documentation.

RPC method parameters
---------------------

Most RPC methods receive parameters.
Per convention **push** methods usually receive an array of objects at a time to improve the synchronization performance.
However, it is usually easier to handle single objects while inserting, as especially products might have large amounts of information that have to be stored at different locations inside the target software system.
The example `Connector` class above therefore uses a simple `foreach` loop to call the respective controller method several times, each time passing one of the objects received from the client.

You can see that there already is one exception of this rule of thumb:
The method `product_price.push` that provides a fast way of updating product prices (an operating that is executed quite often) only receives one object at a time.
This is due to the fact, that price updates happen regularly and should therefore be executed as fast as possible.

.. note::
    The approach depicted above, i.e. passing one object at a time, is in no way being enforced by JTL-Connector.
    You are free to vary your logic, depending on the abilities or requirements of the platform you are addressing.

The controller method results are then collected and returned to :doc:`jtlconnector </glossary/jtlconnector>`.
A so-called `Action` object is created with the results and possible errors that might have occurred during method execution.

