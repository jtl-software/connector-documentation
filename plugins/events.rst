.. _plugin-events:

Events
======

There are two kind of events: the Before and the After Event.
Both can be applied to each of the for controller methods: push, pull, delete and statistics.
Consequential each of the :ref:`data-models` has eight different events which you can subscribe e.g. ProductAfterPushEvent.
One special event is the RPC event which delivers the controller, action and passed data as text.

Each of the events has a reference to the main entity you targeted.
By using this reference it is not just possible to retrieve information but also manipulate the main entity before it passed to the shop database.

The technology behind the event system is explained in the next chapter, see :ref:`plugin-architecture`.
