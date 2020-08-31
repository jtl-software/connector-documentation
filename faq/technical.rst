Technical
=========

**What is logged and where can I find it?**

Read :ref:`Server site debugging <debugging-server>` for detailed information.

**What is the config.json file located in the config folder?**

This file can be used to define configurations you want to access during the sync progress.
The config is passed to the connector.php via the initialize method wich can then be passed further down using the DI container.
A predefined key is ``log`` which cam be used to define a logging level and directory.

**What should be done if an error occurs?**

All Exception that occur within the :doc:`Endpoint </glossary/endpoint>` are being caught by the core and then be passed to the :doc:`JTL-Wawi </glossary/jtl-wawi>`