Technical
=========

**What is logged and where can I find it?**

Read :ref:`Server site debugging <debugging-server>` for detailed information.

**What is the config.json file located in the config folder?**

This file can be used to define configurations you want to access during the sync progress.
The config is passed to the Connector object via the initialize method. You can read more about configuration :ref:`here <configuration>`.

**How can I overwrite model values without changing connector code?**

Please see :ref:`plugins <plugins-introduction>` guide to see how to extend functionality of connector.

**What should be done if an error occurs?**

All Exceptions that occur within the :doc:`endpoint </glossary/endpoint>` are being caught by the :doc:`Core</glossary/core>` and returned in the response to :doc:`JTL-Wawi </glossary/jtl-wawi>`.
If you think this is a bug in software you can let us know by posting new thread in `our forum  <https://forum.jtl-software.de/#jtl-connector.6>`_.