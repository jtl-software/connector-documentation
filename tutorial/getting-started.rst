Getting started
===============

.. note::
    Full example connector implementation is available in our Github repository `connector-example <https://github.com/jtl-software/connector-example>`_

This tutorial provides the necessary information to get you started quickly.
We will show you how to connect :doc:`JTL-Wawi </glossary/jtl-wawi>` to a PHP-based platform and enable it to synchronize data between the two systems.
Although it is not technically required to use PHP for JTL-Connector, this language is the only language we officially support on the server side.

While application environments like ASP.NET or Java can be used as well, you would then be required to implement the complete protocol logic by yourself.
Of course you could mimic the structure of the provided PHP library, but this goes far beyond the scope of this beginner's guide.
We are going to continue using PHP in the course of this book.

Preliminary note
----------------

All code specific for this example, i.e. code that is specific for the targeted software system that should be connected to JTL-Wawi, resides in the `Jtl\\Connector\\Example` namespace.
You have to use a different namespace prefix for your implementation.
A possible approach is to combine your company's name with the system you want JTL-Wawi to connect to.
So if your company was named "ACME Inc." and you wanted to connect to your own hypothetic eCommerce platform called "ACME Shop" a suitable namespace prefix would be `Acme\\Connector\\AcmeShop`.

.. note::
    Consider the `PSR-4 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md>`_ standard document if you have any questions regarding to the naming of PHP namespaces.


Entry point
-----------

Note that some software products require you to create a real plugin along with additional boilerplate code before you are able to pass execution to JTL-Connector.
Consult the developer documentation of the target platform if you are unsure.

During this book we assume that we place a file called index.php inside the directory `public/` which is the document root directory for `http://www.shopdomain.tld/jtlconnector/` and the entry point of the example connector.
It is up to you to make sure that this call succeeds in your environment before you may continue.

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

After the index code initializes the autoloader, you may want to instantiate a custom Config or ConfigSchema object.
At the end of the index.php we then create a Connector object and use it to instantiate the application which then gets started.
If a custom Config or ConfigSchema was created, they should be passed to the application as well. Otherwise the application will create those objects itself.

The application class manages communication between the two system, handles the protocol layer and forwards all valid requests to the :code:`Connector` class.
Its function is to handle these requests and return results back to the application object which wraps the result in the communication protocol and responds to the client.

The application implementation and thus the protocol layer, too, is shared between all PHP-based endpoints.

.. note::
    It is **strongly recommended** to use the official implementation by JTL-Software (i.e. :doc:`jtlconnector </glossary/jtlconnector>`) because it is absolutely necessary for the protocol layer to be compatible with :doc:`JTL-Wawi </glossary/jtl-wawi>`'s expectations.
    Your code only needs to make use of the classes and methods provided by :doc:`jtlconnector </glossary/jtlconnector>`.
