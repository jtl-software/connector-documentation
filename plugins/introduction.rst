.. _plugins-introduction:

Introduction
============

Plugins get invoked by an event driven system.
These events are fired by the :doc:`Core</glossary/core>`.
More detailed information about the event system can be found in chapter :ref:`events <plugin-events>`.

By using the above mentioned principle, the plugin is decoupled from the actual :doc:`endpoint </glossary/endpoint>` implementation.
Nevertheless you have access to all information transferred by :doc:`JTL-Wawi </glossary/jtl-wawi>` and the :doc:`endpoint </glossary/endpoint>`.
