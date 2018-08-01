Technical
=========

**What is logged and where can I find it?**

Read :ref:`Server site debugging <debugging-server>` for detailed information.

**What is the config.json file located in the config folder?**

This file can be used to define configurations you want to access during the sync progress.
They can be access by ``Application()->getConfig()``.
A predefined key is ``developer_logging`` which has the effect, if it is set to true, that also messages with a DEBUG level are logged.

**How can i write an abstract mapper?**

By using the ``jtl\Connector\Type\DataType`` and ``jtl\Connector\Model\DataModel`` class an abstract mapper can be implemented.
An example on how you get the type of the called mapper can be found in the example connector's ``jtl\Connector\Example\Mapper\DataMapper`` class.

**Why are my mappers and controllers not found?**

* It is not intended to add sub namespaces for classes in the controller and mapper folder. If you do so you have to make sure that the namespaces are taken into account while loading the classes.
* You do not stick to the PSR-0 or PSR-4 autoloading standard specified in the composer.json. Check out `this site <http://www.php-fig.org/psr/>`_ for more information.

**What should be done if an error occurs?**

Exceptions has to be caught from within the :doc:`Endpoint </glossary/endpoint>`.
To make that error public to the :doc:`JTL-Wawi </glossary/jtl-wawi>` you have to set an :code:`jtl\Connector\Core\Rpc\Error` on the :code:`jtl\Connector\Result\Action` object which is returned.
