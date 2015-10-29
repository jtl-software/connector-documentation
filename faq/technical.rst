Technical
=========

**What is logged and where can I find it?**

All log files are by default located in a logs folder. It can be found in the connector folder.
By defining the named constant ``LOG_DIR`` the location can also be changed.
All log files listed below are suffixed by the current date in ISO 8601 format and have the file type log.
The content of a log entry is a timestamp followed by the level and the log content itself.
Keep in mind that on a production setting messages with DEBUG as level (checksum, database, rpc and session) are just logged if either the ``developer_logging`` flag explained in the next question is true or your system environment variable ``APPLICATION_ENV`` is set to development.

* checksum: The linking, reading and writing of the checksums are written into this file.
* controller: Any exceptions that occur in the controllers' actions.
* global: Any exceptions are written to this file. They contain the location (class and line) and the message.
* database: If you use one of the specific database classes of ``jtl\Connector\Core\Database`` all your queries will be logged in this file.
* rpc: All requests and responses between JTL-Wawi and endpoint are written into this file.
* session: All actions of the session handler are written into this file.

**What is the config.json file in the config folder?**

This file can be used to define configurations you want to access during the sync progress.
They can be access by ``Application()->getConfig()``.
A predefined key is ``developer_logging`` which has the effect, if it is set to true, that also messages with a DEBUG level are logged.

**What does the following error code/message mean?**

* Code: -32603, Message: Internal error => No action returned

**How can write an abstract mapper?**

By using the ``jtl\Connector\Type\DataType`` and ``jtl\Connector\Model\DataModel`` class an abstract mapper can be implemented.
An example on how you get the type of the called mapper can be found in the example connector's ``jtl\Connector\Example\Mapper\DataMapper`` class.

**Why are my mappers and controllers not found?**

* It is not allowed to add sub namespaces for classes in the controller and mapper folder.
* You do not stick to the PSR-0 or PSR-4 autoloading standard specified in the composer.json. Checkout `this site <http://www.php-fig.org/psr/>`_ for more information.
