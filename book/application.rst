Application
===========

Entry point for each request is the ``Jtl\Connector\Core\Application\Application`` class. To properly serve the request you should
create an instance of a connector application with desired parameters and options and call the ``run`` method.

- ``Jtl\Connector\Core\Connector\ConnectorInterface $connector`` - instance of endpoint
- ``string $connectorDir`` - root path to endpoint
- ``Noodlehaus\ConfigInterface $config`` - (optional) config object for use in core and endpoint
- ``Jtl\Connector\Core\Config\ConfigSchema $configSchema`` - (optional) definition of what config object should have to be valid.
  If you want to know more about the config schema please check the :ref:`configuration <configuration>` chapter

Overwriting defaults
--------------------

The application provides some methods to change default used instances:

- ``setSessionHandler`` - by default the ``Jtl\Connector\Core\Session\SqliteSessionHandler`` is used but it can be replaced
  by another handler. A Symfony session handler could be used for instance.

  .. note::
      If you want to use a Symfony session handler, then you have to create an anonymous class which implements the ``Jtl\Connector\Core\Session\SessionHandlerInterface`` interface and extends the session handler class.

      .. code-block:: php

         $application->setSessionHandler(new class($pdoOrDsn) implements SessionHandlerInterface extends PdoSessionHandler);

- ``setErrorHandler`` - by default ``Jtl\Connector\Core\Error\ErrorHandler`` can be changed to another handler which extends
  ``Jtl\Connector\Core\Error\AbstractErrorHandler`` class.

- ``registerController`` - if you want to register a controller which does not match the default controller name pattern (or any other reason). You can check the constants defined in the class ``Jtl\Connector\Core\Definition\Controller`` for all valid controller names in the :doc:`Core</glossary/core>`.

.. danger::
    Please keep in mind that changing the default behaviour of the core, requires some advanced knowledge about how the core works.

The application class is using a `DI container <https://php-di.org/>`_ for handling objects and dependencies internally. Because of that it is possible to overwrite
most of code functionalities by your own objects.

.. _request_handling:

Request handling
----------------

By default incoming requests are handled by the application in the ``handleRequest`` method. It should contain all required logic to
process the request.

If the ``handleRequest`` method does not match the requirements for your endpoint, it is also possible to handle the request directly in the :doc:`endpoint </glossary/endpoint>`. In order to achieve this, the connector class from the endpoint
must implement the ``Jtl\Connector\Core\Connector\HandleRequestInterface`` interface.


Subscribers (I/O data manipulations)
------------------------------------

We are using some data manipulators to change the input and output data in the :doc:`Core</glossary/core>`. In this case the data manipulations are related
to the de-/serialization of JSON requests and responses.

.. note::
    If you want to know more about handlers and subscribers, please take a look at `jms/serializer <https://jmsyst.com/libs/serializer>`_.

In the serializer builder class ``Jtl\Connector\Core\Serializer\SerializerBuilder``, we are subscribing some events and also using some
handlers. All changes are adapted to current models so there is no need to adapt model properties by your own.

For instance the subscriber ``Jtl\Connector\Core\Serializer\Subscriber\LanguageIsoSubscriber`` is responsible for converting the language
ISO standard from `ISO-639-2/B` to `ISO-639-1` and vice versa.

All translatable core models own a property called ``languageIso`` (`ISO-639-1`). Before a translatable model will be send to JTL-Wawi the ``languageIso`` property must be transformed into
``languageISO`` (`ISO-639-2/B`), because it is standard in JTL-Connector.

The subscriber transforms the language property for de-/serialization, so connector developers do not need to take care about.