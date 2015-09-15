Example Connector
=================

The fastest way of learning is to do it yourself with an example.

index.php
---------

The entry point.

.. code-block:: php

    <?php
    defined('CONNECTOR_DIR') || define("CONNECTOR_DIR", __DIR__);

    include (__DIR__ . "/src/bootstrap.php");

bootstrap.php
-------------

The bootstrap.

.. code-block:: php

    <?php
    require_once (__DIR__ . "/../vendor/autoload.php");

    use jtl\Connector\Application\Application;
    use jtl\Connector\Example\Connector;

    $application = null;

    try {
        // ...

        // Connector instance
        $connector = Connector::getInstance();
        $application = Application::getInstance();
        $application->register($connector);
        $application->run();
    } catch (\Exception $e) {
        if (is_object($application)) {
            $handler = $application->getErrorHandler()->getExceptionHandler();
            $handler($e);
        }
    }

.. toctree::
    :hidden:

    structure

.. include:: /connector/map.rst.inc