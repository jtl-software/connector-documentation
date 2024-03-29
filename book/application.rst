.. _application:

Application
===========

Starting point of each endpoint is the application, which is an instance of the class ``Jtl\Connector\Core\Application\Application``. The application has three constructor arguments:

    - ``string $connectorDir`` - root path to endpoint
    - ``Noodlehaus\ConfigInterface $config`` - (optional) config object for use in core and endpoint
    - ``Jtl\Connector\Core\Config\ConfigSchema $configSchema`` - (optional) definition of what config object should have to be valid.

      .. note::

        More details about the config schema can be found in the :ref:`configuration <configuration>` chapter.


A connector related request can be properly served by calling the ``run`` method from the application. Required argument is an instance of a class which implements the ``Jtl\Connector\Core\Connector\ConnectorInterface`` interface. The connector implementation provides required data about the endpoint.

.. code-block:: php

    $application->run($connector);



Overriding defaults
--------------------

The application provides some methods to replace the default used instances:

- ``setSessionHandler`` - by default the ``Jtl\Connector\Core\Session\SqliteSessionHandler`` is used but it can be replaced
  by another handler. A Symfony session handler could be used for instance.

  .. note::
      If you want to use a Symfony session handler, then you can create an anonymous class which implements the ``Jtl\Connector\Core\Session\SessionHandlerInterface`` interface and extends the session handler class.

      .. code-block:: php

         $application->setSessionHandler(new class($pdoOrDsn) implements SessionHandlerInterface extends PdoSessionHandler);

- ``setErrorHandler`` - by default an instance of ``Jtl\Connector\Core\Error\ErrorHandler`` is set. It can be replaced by another handler which extends
  ``Jtl\Connector\Core\Error\AbstractErrorHandler``.

- ``registerController`` - if you want to register a controller which does not match the default controller name pattern (or any other reason). You can check the constants defined in the class ``Jtl\Connector\Core\Definition\Controller`` for all valid controller names in the :doc:`Core</glossary/core>`.

.. danger::
    Please keep in mind that changing the default behaviour of the core requires some advanced knowledge about how the core works.

The application is using a `DI container <https://php-di.org/>`_ for handling objects and dependencies internally.
Because of this, it is possible to override most of code functionalities by your own objects.

.. _request_handling:

Request handling
----------------

Incoming requests are handled by the application in the ``handleRequest`` method by default. It should contain all required logic to process the request.

If the ``handleRequest`` method does not match the requirements for your endpoint, it is also possible to handle the request directly in the :doc:`endpoint </glossary/endpoint>`. In order to achieve this, the connector class from the endpoint
must implement the ``Jtl\Connector\Core\Connector\HandleRequestInterface`` interface.


Subscribers (I/O data manipulations)
------------------------------------

We are using some data manipulators to change the input and output data in the :doc:`Core</glossary/core>`. In this case the data manipulations are related
to the de-/serialization of JSON requests and responses.

.. note::
    If you want to know more about handlers and subscribers, please take a look at `jms/serializer <https://jmsyst.com/libs/serializer>`_.

In the ``Jtl\Connector\Core\Serializer\SerializerBuilder`` class are some events subscribed and
handlers added, for being able to properly de-/serializing the :doc:`Core</glossary/core>` models. All manipulations are adapted to the current models so there is no need to modify model properties by your own.

For instance the subscriber ``Jtl\Connector\Core\Serializer\Subscriber\LanguageIsoSubscriber`` is responsible for converting the language
ISO standard from `ISO-639-2/B` to `ISO-639-1` and vice versa.

All translatable core models own a property called ``languageIso`` (`ISO-639-1`). Before a translatable model will be send to JTL-Wawi the ``languageIso`` property must be transformed into
``languageISO`` (`ISO-639-2/B`), because it is standard in JTL-Connector.

The subscriber transforms the language property for de-/serialization, so connector developers do not need to take care about.