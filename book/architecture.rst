.. _connector-architecture:

Architecture
============

The interface between :doc:`JTL-Wawi </glossary/jtl-wawi>` and :doc:`JTL-Connector </glossary/jtl-connector>` consists of two layers.
The first layer - provided by JTL-Software - is called :doc:`Core</glossary/core>`.

.. image:: /_images/connector_flow.png

`jtlconnector` arbitrates between :doc:`JTL-Wawi </glossary/jtl-wawi>` and your so-called **endpoint** logic.
Your endpoint is the last piece of code and bridges between :doc:`Core</glossary/core>` and your target system.

To achieve this, JTL-Connector makes use of the widely known MVC pattern.
:doc:`Core</glossary/core>` provides the models and the view layer.
Your opportunity is to provide the appropriate controller code to read data from or write data to your target system.