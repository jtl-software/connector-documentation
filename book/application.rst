Application
===========

Entry point for each request is ``Jtl\Connector\Core\Application\Application`` class. To properly serve request you should
create instance of application with desired parameters and options and call ``run`` method.

- ``Jtl\Connector\Core\Connector\ConnectorInterface $connector`` - instance of endpoint
- ``string $connectorDir`` - root path to endpoint
- ``Noodlehaus\ConfigInterface $config`` - (optional) config object for later use in core and connector
- ``Jtl\Connector\Core\Config\ConfigSchema $configSchema`` - (optional) definition of what config object should have to be valid.
  If you want to know more about config schema please check :ref:`config schema chapter <config-schema>`


Subscribers (I/O data manipulations)
------------------------------------

We are using some data manipulators to made changes in input or output data. In this case data manipulations is related
to serialize and deserialize JSON requests.

.. note::
    If you want to know more about handlers and subscribers please take a look at `jms/serializer <https://jmsyst.com/libs/serializer>`_.

In serializer builder class ``Jtl\Connector\Core\Serializer\SerializerBuilder`` we are subscribing some events and also using some
handlers. All changes are adapted to current models so there is no need to adapt model properties by your own.

For example subscriber: ``Jtl\Connector\Core\Serializer\Subscriber\LanguageIsoSubscriber`` is responsible for language
ISO standard converting from `ISO-639-2/B` to `ISO-639-1` and revert.

In models you work with property called ``languageIso`` (`ISO-639-1`) but before it's sent to Wawi we must change it back to
``languageISO`` (`ISO-639-2/B`) because it's Wawi standard.

Subscriber is doing it after serialize and before deserialize so connector developer don't need to do that.


Overwriting defaults
--------------------

Application provide some functions to change default used classes, please take a look at this functions and short
explanation:

- ``setSessionHandler`` - by default ``Jtl\Connector\Core\Session\SqliteSessionHandler`` is used but you can override it
  by some other handler for example Symfony session handler

- ``setErrorHandler`` - by default ``Jtl\Connector\Core\Error\ErrorHandler`` can be changed to other handler that implements
  ``Jtl\Connector\Core\Error\AbstractErrorHandler``.

- ``registerController`` - you can register your own controller class. Only requirement is that it you need to register
  it by valid controller name, you can check it in Controller definitions

.. danger::
    Please keep in mind that changing default behaviour of core requires some advance knowledge about how core works.

Application class is using DI container to manage objects inside in easy way. Because of that it's possible to overwrite
most of code functionalities by your own objects.

What can be overwritten?:

- IdentityLinker
- ChecksumLinker
- ChecksumLoader
- PrimaryKeyMapper
- TokenValidator
- SessionHandler
- Config
- LoggerService
- Logger