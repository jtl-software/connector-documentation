.. _plugin-architecture:

Architecture
============

Regarding the architecture the general structure is explained in the next section as well as a detailed explanation of the EventDispatcher used to realize the event driven aspect of the plugin system.

Integration into architecture
-----------------------------

If we take the already explained architecture from :ref:`connector-architecture`, we can add a third layer, the Plugin.
From within the application either the Before Event is fired before the request is handled by the :doc:`Endpoint </glossary/endpoint>` or the After Event is fired after the endpoint handled it.
This way of architecture decouples :doc:`Endpoint </glossary/endpoint>` and plugin so that none of them has to know about the other.

.. image:: /_images/plugin_flow.png


Symfony EventDispatcher
-----------------------

The Symfony EventDispatcher is a library for sending events between different components of your software.
If you adopt the diagram from below to the Connector the Producer is the Application, the Mediator is the EventDispatcher and the Consumer classes implementing our :code:`PluginInterface` interface, see :ref:`plugin-bootstrap`.
As you can see it is possible to have more than one listener for the same kind of event.

.. image:: /_images/plugin_events.png

Checkout `this site <http://symfony.com/doc/current/components/event_dispatcher/introduction.html>`_ for more information about the Symfony EventDispatcher.
