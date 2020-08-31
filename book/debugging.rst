.. _debugging:

Debugging
=========

There are two ways of debugging your :doc:`Endpoint </glossary/endpoint>`.

.. _debugging-server:

Server side
-----------

The :doc:`JTL-Connector </glossary/jtl-connector>` writes its own log files.
All log files are by default located in a var/log folder. It can be found in the connector folder.
Log directory can be set in config.json by ``log_dir`` parameter.
All log files listed below are suffixed by the current date in ISO 8601 format and have the file type log.
The content of a log entry is a timestamp followed by the level and the log content itself.
Keep in mind that on a production setting messages with DEBUG as level (checksum, database, rpc and session) are just logged if either the ``debug`` flag in the config.json file is true.

* checksum: The linking, reading and writing of the checksums are written into this file.
* global: Any log information from endpoint controller is written into this file
* error: Exceptions that are thrown are written into this file
* linker: Identity linker related information
* rpc: All requests and responses between JTL-Wawi and endpoint are written into this file.
* session: All actions of the session handler are written into this file.

Other channels can be added as well as the log level can be defined.

.. image:: /_images/debugging_server.png

Using RPC viewer plugin
-----------------------

Special plugin that is event based and listen for RPC calls before and after action can also be used. Plugin has GUI
interface that shows in realtime communication between client and :doc:`endpoint </glossary/endpoint>`. In order to use it you need to put it
inside ``plugins`` folder and open url that points into that directory like http://acme-shop.com/{path_to_connector}/plugins/rpcview/index.html

You can find this plugin in our `github repository <https://github.com/jtl-software/connector-plugin-rpcviewer>`_

.. image:: /_images/rpc_viewer.png

Client side
-----------

On client side the 'Connector Tester' tool can be used.
It shows the direct RPC output in form of JSON, tree like structure or HTML.
The response time is shown as well.
All available RPC calls can be tested with this software.
It is very useful if you are at the beginning of you endpoint or plugin implementation.
The tester does not save mappings which means that you do not have to delete them every time you want to test the pull or statistics method.

.. image:: /_images/debugging_client.png
