Technical
=========

**What is logged and where can I find it?**

Read :ref:`Server site debugging <debugging-server>` for detailed information.

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
