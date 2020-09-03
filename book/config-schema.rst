.. _config-schema:

Config Schema
=============

The config schema is used to define the structure of the config for the endpoint implementation. There are a few parameters which are already defined and required by the application.

============= ========= =================================
Option        Data type Default value
============= ========= =================================
cache_dir     string    "{connector_dir}/var/cache"
connector_dir string    "{connector_dir}"
debug         boolean   false
features_path string    "{connector_dir}/config/features"
log.level     string    "info"
log.format    string    "line"
log_dir       string    "{connector_dir}/var/log"
main_language string    "de"
plugins_dir   string    "{connector_dir}/plugins"
============= ========= =================================

Default parameter values can be changed in the configuration (ie. in config/config.json).

.. note::
    The :code:`connector_dir` parameter will be set one time when the application is getting instantiated and can not be changed afterwards. It can not be set in the configuration.

.. warning::
    Changing values from the default parameters should be done with caution.