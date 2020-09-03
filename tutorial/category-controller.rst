Category controller
===================

Category controller is one of many main controllers others are for example: Product, Manufacturer, Customer, CustomerOrder etc.
Example connector contain implementation of all basic methods that can be called in controller:

.. note::
    You can read more about request flow here: :ref:`fundamentals`

- statistic
- pull
- push
- delete

.. note::
    In example connector we decided to use `UUID's <https://de.wikipedia.org/wiki/Globally_Unique_Identifier>`_ to create
    ids. However if you creating your own connector it's up to you what to use. Please also see how :ref:`primary-key-mapper` works.

Here is example json payload that you can send into connector (for example by :ref:`connector tester <debugging-client-side>`) to create new category with two translations:

.. code::

        [
          {
            "attributes": [],
            "customerGroups": [],
            "i18ns": [
              {
                "categoryId": [
                  "",
                  1
                ],
                "languageISO": "ger",
                "name": "Katalog #1",
                "description": "",
                "urlPath": "",
                "metaDescription": "",
                "titleTag": "",
                "metaKeywords": ""
              },
              {
                "categoryId": [
                  "",
                  1
                ],
                "languageISO": "eng",
                "name": "Catalogue #1",
                "description": "",
                "urlPath": "",
                "metaDescription": "",
                "titleTag": "",
                "metaKeywords": ""
              }
            ],
            "invisibilities": [],
            "level": 0,
            "entityType": "Category",
            "id": [
              "",
              1
            ],
            "parentCategoryId": [
              "",
              0
            ],
            "isActive": true,
            "sort": 0
          }
        ]