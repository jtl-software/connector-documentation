.. _plugin-events:

Events
======

Events are dispatched in :doc:`Application </book/application>` class in specific moments and can be classified as 4 main types by event name creation.
You can easily build event name using static helper methods from ``Jtl\Connector\Core\Definition\Event`` class.
By using events you can add functionality to the main entities which themselves cannot be added. The technology behind the
event system is explained in the next chapter, see :ref:`plugin-architecture`.

1. Endpoint controller related
------------------------------

This is most common event type. Can be used for model properties manipulations. Events listed below are related to
main model entities. If event class is missing then ``Jtl\Connector\Core\Event\ModelEvent`` will be used.

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

This event type is connector core events related. Can be used if you want to override data
that is send by connector core to client or in opposite direction.

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

Handle events are fired before and after specific request in 'handled' by Application or by Connector (depends on implementation).

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

There are two RPC events in Application that you can subscribe. They are called before serialization and before
response is sent.

Event: ``Jtl\Connector\Core\Event\RpcEvent``

How to create name for this event?

.. code-block:: php

    use Jtl\Connector\Core\Definition\Event;

    Event::createRpcEventName(Event::BEFORE);
