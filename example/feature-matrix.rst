The feature matrix
==================

It is very likely that your endpoint implementation does not support the full feature set JTL-Wawi offers.
This might be due to limitations of the underlying target system or because of functionality that cannot be made compatible with JTL-Wawi because their respective concepts differ too much.
To tell JTL-Wawi which features of JTL-Connectors are supported by your endpoint implementation, JTL-Connector requires you to build a **feature matrix** and ship it with your endpoint code.

Basically, this is a simple JSON file containing information about which features are supported or not.
An excerpt of the example connector's feature matrix is shown below to give you an idea of the basic concept behind this file.
The complete file is available on `GitLab <https://gitlab.jtl-software.de/jtlconnector/example-connector/blob/master/config/features.json>`_.

.. code-block:: json

    {
        "entities": {
            "Category": {
                "pull": true,
                "push": true,
                "delete": true
            },
            "CategoryAttr": {
                "pull": true,
                "push": true,
                "delete": true
            },
            "CategoryAttrI18n": {
                "pull": true,
                "push": true,
                "delete": true
            },
            "CategoryI18n": {
                "pull": true,
                "push": true,
                "delete": true
            },
            "CategoryInvisibility": {
                "pull": true,
                "push": true,
                "delete": true
            },
            "CrossSellingGroup": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CrossSellingGroupI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Currency": {
                "pull": true,
                "push": false,
                "delete": false
            },
            "Customer": {
                "pull": true,
                "push": true,
                "delete": true
            },
            "CustomerAttr": {
                "pull": false,
                "push": false,
                "delete": false
            }
        },
        "flags": {
            "var_combination_child_first": false,
            "product_images_supported": true,
            "category_images_supported": true,
            "manufacturer_images_supported": true,
            "specific_images_supported": false,
            "specific_value_images_supported": false,
            "config_group_images_supported": false,
            "product_variation_value_images_supported": false,
            "variation_products_supported": false,
            "variation_combinations_supported": true,
            "set_articles_supported": false,
            "needs_finish_call": false,
            "free_field_supported": false
        }
    }

The file divides into two main parts.
The first part lists the supported object types together with information in which context they can be used (e.g. whether they can be updated by JTL-Wawi or are read-only and whether they can be deleted programmatically).

Special function flags
----------------------

The second part sets special function flags.
These flags become important when your target system e.g. needs to receive information in a special order.

An example is the creation of variation combinations, i.e. configurable products specified in a parent-child relationship.
Some systems need to have all available child products before the parent product may be created, maybe, because the parent product must be equipped with a list of all available child products.
Other systems might need to create the parent product first, e.g. because all child products keep track of their master by using some kind of database foreign key that has to exist.

Either way, you are able to influence JTL-Wawi's behaviour when preparing its operations by configuring your function flags correctly.
Most of the flag names are pretty self-explanatory.
Some of these require a deep understanding of the targeted system to decide which value to set for a certain function flag.

+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Flag                        | Description                                                                                                                                                              |
+=============================+==========================================================================================================================================================================+
| var_combination_child_first | Used to determine whether child products or parent products must be inserted first when uploading variation combination from JTL-Wawi.                                   |
|                             | A `true` value determines that the child product will be inserted first and the parent products will be the last products during the complete synchronization operation. |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| needs_finish_call           | Specifies that this endpoint needs to perform maintenance tasks after the synchronization has completed.                                                                 |
|                             | This mechanism can be used to recreate frontend indexes that might be needed after product data update.                                                                  |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
