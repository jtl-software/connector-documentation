.. _plugin-events:

Events
======

Every event is generated on the fly for all calls that are processed by the connector and consist of the pats:
An order like "Before" or "After"
A controller like "Category" or "Product"
An action like "Push" or "Pull"

Consequential each of the :ref:`data-models` has eight different events which you can subscribe e.g. ProductAfterPushEvent.
Using the Event::createEventName() function you can define an eventname to be registered in the application.
Alternatively, if you want to create plugins on a more general scale, you can use the Event::createHandleEventName() function.

Besides the events for the entities there is a special event, the ``CoreConnectorAfterFeaturesEvent``.
By using this event you can add functionality to the main entities which themselves cannot be added.

The technology behind the event system is explained in the next chapter, see :ref:`plugin-architecture`.
