.. _plugins-introduction:

Introduction
============

Plugins get invoked by an event driven system.
These events are fired by the Connector-Core.
More detailed information about the event system can be found in chapter :ref:`plugin-events`.

Another programming paradigm which is used is Dependency Injection.
It allows the automatically loading of all plugins by the Connector-Core.

By using the above mentioned principles the plugin is decoupled from the actual :doc:`Endpoint </glossary/endpoint>` implementation.
Nevertheless you have access to all by the :doc:`JTL-Wawi </glossary/jtl-wawi>` transferred information.
