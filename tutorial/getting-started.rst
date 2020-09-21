Getting started
===============

.. note::
    The full connector implementation of our tutorial is available on `Github <https://github.com/jtl-software/connector-example>`_.

This tutorial provides necessary information to get you started quickly.
We will explain how to connect :doc:`JTL-Wawi </glossary/jtl-wawi>` to a PHP-based platform as well as how to synchronize data between the two systems.
Although it is not technically required to use PHP for JTL-Connector, this language is the only language we officially support on server side.

While application environments like ASP.NET or Java can be used as well, you would then be required to implement the complete protocol logic by yourself.
Of course you could mimic the structure of the provided PHP library, but this goes far beyond the scope of this tutorial.
We are going to continue using PHP in the course of this book.

Preliminary note
----------------

All code specific for this tutorial, i.e. code that is specific for the targeted software system that should be connected to JTL-Wawi, resides in the ``Jtl\\Connector\\Example`` namespace.
You have to use a different namespace prefix for your implementation.
A possible approach is to combine your company's name with the system you want to connect with JTL-Wawi.
So if your company's name is "ACME Inc." and you want to connect to your own hypothetical eCommerce platform called "ACME Shop", a suitable namespace prefix would be ``Acme\\Connector\\AcmeShop``.

.. note::
    Consult the `PSR-4 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md>`_ standard document if you have any questions regarding to the naming of PHP namespaces.


Entry point
-----------

.. note::
    Some software products require you to create a real plugin along with additional boilerplate code, before you are able to pass execution to JTL-Connector.
    Consult the developer documentation of the target platform if you are unsure.

The entry point for the connector in this tutorial is a file called ``public/index.php``. It will be executed when the url ``https://www.shopdomain.tld/jtlconnector`` is requested.
It is up to you to make sure that this call succeeds in your environment before you may continue.

.. note::
    ``www.shopdomain.tld`` is a placeholder for a valid domain.

.. code-block:: php

    <?php

   $connectorDir = dirname(__DIR__);

    require_once $connectorDir . "/vendor/autoload.php";

    use Jtl\Connector\Core\Application\Application;
    use Jtl\Connector\Core\Config\ConfigParameter;
    use Jtl\Connector\Core\Config\ConfigSchema;
    use Jtl\Connector\Core\Config\FileConfig;
    use Jtl\Connector\Example\Connector;

    $application = null;

    //Setting up a custom FileConfig passing the needed File
    $config = new FileConfig(sprintf('%s/config/config.json', $connectorDir));

    //Setting up a custom config schema that checks the config file for the defined properties
    $configSchema = (new ConfigSchema)
        ->setParameter(new ConfigParameter("token", "string", true))
        ->setParameter(new ConfigParameter("db.host", "string", true))
        ->setParameter(new ConfigParameter("db.name", "string", true))
        ->setParameter(new ConfigParameter("db.username", "string", true))
        ->setParameter(new ConfigParameter("db.password", "string", true));

    //Instantiating the Connector class which holds information and acts like a Toolbox the the application
    $connector = new Connector();

    //Instantiating and starting the Application as the highest instance of the Connector passing every custom object as well as the connector object
    $application = new Application($connector, $connectorDir, $config, $configSchema);
    $application->run();

After the the autoloader is initialized, a custom Config and/or a ConfigSchema object may want to instantiated. Both is optional.

At the end of the script we then create a Connector object and use it to instantiate the application which then gets started.


If a custom Config or ConfigSchema was created, they should be passed to the application as well. Otherwise the application will create those objects itself.

The application class manages communication between the two system, handles the protocol layer and forwards all valid requests to the :code:`Connector` class.
Its function is to handle these requests and return results back to the application object which wraps the result in the communication protocol and responds to the client.

The application implementation and thus the protocol layer, too, is shared between all PHP-based endpoints.

.. note::
    It is **strongly recommended** to use the official implementation by JTL-Software, because it is absolutely necessary for the protocol layer to be compatible with :doc:`JTL-Wawi </glossary/jtl-wawi>`.
    Your endpoint implementation just needs to make use of the classes and methods provided by the :doc:`Core</glossary/core>`.
