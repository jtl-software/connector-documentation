.. _debugging:

Debugging
=========

There are two ways of debugging your :doc:`Endpoint </glossary/endpoint>`.

.. _debugging-server:

Server side
-----------

The :doc:`JTL-Connector </glossary/jtl-connector>` writes its own log files.
All log files are by default located in a logs folder. It can be found in the connector folder.
By defining the named constant ``LOG_DIR`` the location can also be changed.
All log files listed below are suffixed by the current date in ISO 8601 format and have the file type log.
The content of a log entry is a timestamp followed by the level and the log content itself.
Keep in mind that on a production setting messages with DEBUG as level (checksum, database, rpc and session) are just logged if either the ``developer_logging`` flag in the config.json file is true or your system environment variable ``APPLICATION_ENV`` is set to development.

* checksum: The linking, reading and writing of the checksums are written into this file.
* controller: Any exceptions that occur in the controllers' actions.
* global: Any exceptions are written to this file. They contain the location (class and line) and the message.
* database: If you use one of the specific database classes of ``jtl\Connector\Core\Database`` all your queries will be logged in this file.
* rpc: All requests and responses between JTL-Wawi and endpoint are written into this file.
* session: All actions of the session handler are written into this file.

Other channels can be added as well as the log level can be defined.

.. image:: /_images/debugging_server.png

Client side
-----------

On client side the 'Connector Tester' tool can be used.
It shows the direct RPC output in form of JSON, tree like structure or HTML.
The response time is shown as well.
All available RPC calls can be tested with this software.
It is very useful if you are at the beginning of you endpoint or plugin implementation.
The tester does not save mappings which means that you do not have to delete them every time you want to test the pull or statistics method.

.. image:: /_images/debugging_client.png
