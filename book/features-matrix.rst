.. _features-matrix:

Features matrix
===============

It is very likely that your endpoint implementation does not support the full feature set JTL-Wawi offers.
This might be due to limitations of the underlying target system or because of functionality that cannot be made compatible with JTL-Wawi because their respective concepts differ too much.
To tell JTL-Wawi which features of JTL-Connector are supported by your endpoint implementation, you are required to build a **features matrix** and ship it with your endpoint code.

Basically, this is a simple JSON file containing information about which features are supported or not.
An example of a connector's features matrix is shown below to give you an idea of the basic concept behind this file.
The file is also available on `GitHub <https://github.com/jtl-software/connector-example/blob/master/config/features.json>`_.

.. code-block:: json

    {
        "entities": {
            "Category": {
                "pull": true,
                "push": true,
                "delete": false
            },
            "CategoryAttr": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CategoryAttrI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CategoryCustomerGroup": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CategoryI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CategoryInvisibility": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Checksum": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ConfigGroup": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ConfigGroupI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ConfigItem": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ConfigItemI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ConfigItemPrice": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CrossSelling": {
                "pull": false,
                "push": false,
                "delete": false
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
            "CrossSellingItem": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Currency": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Customer": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerAttr": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerGroup": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerGroupAttr": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerGroupI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerGroupPackagingQuantity": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrder": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrderAttr": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrderBillingAddress": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrderItem": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrderItemVariation": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrderPaymentInfo": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "CustomerOrderShippingAddress": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "DeliveryNote": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "DeliveryNoteItem": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "DeliveryNoteItemInfo": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "FileDownload": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "FileDownloadI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "FileUpload": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "FileUploadI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Image": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Language": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Manufacturer": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ManufacturerI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "MeasurementUnit": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "MeasurementUnitI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "MediaFile": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "MediaFileAttr": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "MediaFileAttrI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "MediaFileI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "PartsList": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Payment": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Product": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Product2Category": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductAttr": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductAttrI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductConfigGroup": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductFileDownload": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductInvisibility": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductPartsList": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductPrice": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductPriceItem": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductSpecialPrice": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductSpecialPriceItem": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductSpecific": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductStockLevel": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductType": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVarCombination": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariation": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationInvisibility": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationValue": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationValueDependency": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationValueExtraCharge": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationValueI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductVariationValueInvisibility": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ProductWarehouseInfo": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Shipment": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "ShippingClass": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Specific": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "SpecificI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "SpecificValue": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "SpecificValueI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Statistic": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "StatusChange": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "TaxClass": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "TaxRate": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "TaxZone": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "TaxZoneCountry": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Unit": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "UnitI18n": {
                "pull": false,
                "push": false,
                "delete": false
            },
            "Warehouse": {
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
            "free_field_supported": false,
            "needs_category_root": false,
            "translated_attributes_supported": false,
            "send_all_acks": false,
            "disable_statistics": false
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

Nevertheless, you are able to influence JTL-Wawi's behaviour when preparing its operations by configuring your function flags correctly.
Most of the flag names are pretty self-explanatory.
Some of them require a deep understanding of the targeted system to decide which value to set for a certain function flag.

+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Flag                                       | Description                                                                                                                                                                    |
+=============================+===============================================================================================================================================================================================+
| var_combination_child_first                | Used to determine whether child products or parent products must be inserted first when uploading variation combination from JTL-Wawi.                                         |
|                                            | A :code:`true` value determines that the child product will be inserted first and the parent products will be the last products during the complete synchronization operation. |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| product_images_supported                   | Determine if product images are supported by connector.                                                                                                                        |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| category_images_supported                  | Determine if category images are supported by connector.                                                                                                                       |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| manufacturer_images_supported              | Determine if manufacturer images are supported by connector.                                                                                                                   |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| specific_images_supported                  | Determine if specific images are supported by connector.                                                                                                                       |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| specific_value_images_supported            | Determine if specific value images are supported by connector.                                                                                                                 |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| config_group_images_supported              | Determine if config group images are supported by connector.                                                                                                                   |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| product_variation_value_images_supported   | Determine if product variation value images are supported by connector.                                                                                                        |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| variation_products_supported               | Determine if simple variation for product are supported.                                                                                                                       |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| variation_combinations_supported           | Determine if variation combinations for product are supported.                                                                                                                 |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| set_articles_supported                     | Determine if set articles for product are supported.                                                                                                                           |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| free_field_supported                       | Determine if custom fields are supported.                                                                                                                                      |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| needs_category_root                        | If set to :code:`true` JTL-Wawi will send each time category root on `category.push`                                                                                           |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| translated_attributes_supported            | Determine if translated attributes are supported                                                                                                                               |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| send_all_acks                              | If set to :code:`true` JTL-Wawi will send ack for all pull requests                                                                                                            |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| disable_statistics                         | Determine if JTL-Wawi will call statistics before pull call                                                                                                                    |
+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
