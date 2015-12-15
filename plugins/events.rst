.. _plugin-events:

Events
======

There are two kind of events: the Before and the After Event.
Both can be applied to each of the for controller methods: push, pull, delete and statistics.
Consequential each of the :ref:`data-models` has eight different events which you can subscribe e.g. ProductAfterPushEvent.

Each of the events has a reference to the main entity you targeted.
By using this reference it is not just possible to retrieve information but also manipulate the main entity before it passed to the shop database.

Besides the events for the entities there are two special events.
The first one is the RPC event which delivers the controller, action and passed data as text.
As a second special event the ``CoreConnectorAfterFeaturesEvent`` exists.
By using this event you can add functionality to the main entities which themselves cannot be added.

The technology behind the event system is explained in the next chapter, see :ref:`plugin-architecture`.
