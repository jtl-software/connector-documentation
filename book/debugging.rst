.. _debugging:

Debugging
=========

There are two ways of debugging an :doc:`endpoint </glossary/endpoint>`.

.. _debugging-server:

Server side
-----------

The :doc:`endpoint </glossary/endpoint>` writes its own log files.
All log files are located in ``{connector_dir}/var/log`` by default.
The log directory can be changed in the :doc:`configuration </book/configuration>` by using the ``log_dir`` parameter.
The content of a log entry is a timestamp followed by the level and the log content itself.

.. note::
    Keep in mind that DEBUG messages (checksum, database, rpc and session) are only logged when the log level in the configuration (``log.level``) is set to ``debug``.

Log format and log level can be defined in the :doc:`configuration </book/configuration>` as well.

Valid log formats are

* json
* html
* line (default)
* mongoDB

.. note::
    See "`Formatters <https://github.com/Seldaek/monolog/blob/master/doc/02-handlers-formatters-processors.md#formatters>`_" from the Monolog repository if you want to find out about all possible formats.

Valid log levels are

* alert
* critical
* debug
* emergency
* error
* info (default)
* notice
* warning

All default log files listed below are suffixed by the current date in ISO 8601 format and have the file extension log.

* checksum: The linking, reading and writing of the checksums are written into this file.
* global: Any log information from endpoint controller is written into this file
* error: Exceptions that are thrown are written into this file
* linker: Identity linker related information
* rpc: All requests and responses between JTL-Wawi and endpoint are written into this file.
* session: All actions of the session handler are written into this file.

More channels can be added by using the logger service from the application. A new log channel can simply created by calling the get method from the logger service with the channel name.

.. code-block:: php

    $logger = $application->getLoggerService()->get("my-log-channel");

    $logger->info("Something interesting");


.. image:: /_images/debugging_server.png


RPC viewer plugin
-----------------

The RPC viewer is an event based plugin, which is listening for RPC calls before and after an action is executed. It has a web interface
that shows the communication between client and :doc:`endpoint </glossary/endpoint>` in realtime. In order to use it, you need to put it
inside the ``{connector_dir}/plugins/RpcViewer`` directory, which has to be accessed over a web server.

You can find the plugin on `GitHub <https://github.com/jtl-software/connector-plugin-rpcviewer>`_.

.. image:: /_images/rpc_viewer.png

.. _debugging-client-side:

Client side
-----------

On client side the 'Connector Tester' tool for Windows can be used.
It shows the direct RPC output in form of a JSON tree structure or HTML.
The response time is shown as well.
All available RPC calls can be tested with this software.
It can be very useful when you just started to implement an endpoint or a connector plugin as well as for debugging or testing purposes.
The tester does not send connector ACKs to the endpoint automatically, so you do not have to delete the mappings every time you want to test a pull or statistics request.

The Connector tester can be downloaded `here <https://downloads.jtl-connector.de/tester/connector-tester.zip>`_.

.. image:: /_images/debugging_client.png
