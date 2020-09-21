.. _plugin-events:

Events
======

Events are dispatched in an instance of the :doc:`Application </book/application>` class in specific moments.
They can be classified as 4 main types by event name creation.
The technology behind the event system is explained in the next chapter, see :ref:`plugin-architecture`.
You can easily build an event name by using static helper methods from the ``Jtl\Connector\Core\Definition\Event`` class.

1. Endpoint controller related
------------------------------

This is the most common event type. It can be used for the manipulation of models. The classes listed below are used as event arguments related to a specific
Core model. If an event class for a specific model is missing then an instance of ``Jtl\Connector\Core\Event\ModelEvent`` will be used as argument.

Example events ( see full list in `/src/Event` folder ):

- ``Jtl\Connector\Core\Event\CategoryEvent``
- ``Jtl\Connector\Core\Event\CrossSellingEvent``
- ``Jtl\Connector\Core\Event\SpecificEvent``

How to create name for this event?

.. code-block:: php

    use Jtl\Connector\Core\Definition\Action;
    use Jtl\Connector\Core\Definition\Controller;
    use Jtl\Connector\Core\Definition\Event;

    Event::createEventName(Controller::PRODUCT, Action::PULL, Event::BEFORE);


2. Core controller events
-------------------------

This event type is connector core events related. It can be used if you want to override data
which is sent by connector core to a client or in opposite direction.

Event examples:

- ``Jtl\Connector\Core\Event\FeaturesEvent``
- ``Jtl\Connector\Core\Event\BoolEvent``
- ``Jtl\Connector\Core\Event\ModelEvent``

How to create name for this event?

.. code-block:: php

    use Jtl\Connector\Core\Definition\Action;
    use Jtl\Connector\Core\Definition\Controller;
    use Jtl\Connector\Core\Definition\Event;

    Event::createCoreEventName(Controller::CONNECTOR, Action::FEATURES, Event::AFTER);

3. Handle events
----------------

Handle events are fired before and after a specific request is 'handled' by the :doc:`Core</glossary/core>` or by the :doc:`endpoint </glossary/endpoint>` (depends on implementation).

Events:

- ``Jtl\Connector\Core\Event\RequestEvent`` (before handle)
- ``Jtl\Connector\Core\Event\ResponseEvent`` (after handle)

How to create name for this event?

.. code-block:: php

    use Jtl\Connector\Core\Definition\Action;
    use Jtl\Connector\Core\Definition\Controller;
    use Jtl\Connector\Core\Definition\Event;

    Event::createHandleEventName(Controller::PRODUCT, Action::PULL, Event::PULL);

4. RPC event
------------

There are two RPC events in the :doc:`Core</glossary/core>` that you can subscribe. They are called before serialization and before
response is sent.

Event: ``Jtl\Connector\Core\Event\RpcEvent``

How to create name for this event?

.. code-block:: php

    use Jtl\Connector\Core\Definition\Event;

    Event::createRpcEventName(Event::BEFORE);
