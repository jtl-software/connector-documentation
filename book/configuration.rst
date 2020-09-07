.. _config-schema:

Configuration
=============

The class ``Jtl\Connector\Core\Config\ConfigSchema`` is used to define the structure of the configuration for the endpoint. It consists of a collection of parameters. A parameter is defined by the ``Jtl\Connector\Core\Config\ConfigParameter`` class on the other hand.

The following parameters are already defined and required by the :doc:`core </glossary/core>`:

============= ========= ======================================
Option        Data type Default value
============= ========= ======================================
cache_dir     string    "{connector_dir}/var/cache"
connector_dir string    "{connector_dir}"
debug         boolean   false
features_path string    "{connector_dir}/config/features.json"
log.level     string    "info"
log.format    string    "line"
log_dir       string    "{connector_dir}/var/log"
main_language string    "de"
plugins_dir   string    "{connector_dir}/plugins"
============= ========= ======================================

More parameters can be defined in the endpoint if needed.
Default parameter values can be changed in the configuration.

The configuration values itself are managed by an instance of a class which implements the ``Noodlehaus\ConfigInterface`` interface. By default it is reading the values from the file ``config/config.json``. If a configuration value is missing then the default value from the config parameter will be used.

.. note::
    The :code:`connector_dir` parameter has to be defined one time when the application is getting instantiated and can not be changed afterwards. It can not be set in the configuration.

.. warning::
    Changing values from the default parameters should be done with caution.