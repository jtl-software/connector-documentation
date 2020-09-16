Database schema
===============

In our tutorial the connector needs a place to store data for the shop and the mappings. In this case we will use MySQL and a file that
already contains a ready to use schema ``scripts/schema.sql``. All tables represent the shop database, except the table ``mapping``. It is the place
where objects inside JTL-Wawi with the same objects in the shop are getting linked.

Assuming that valid database connection parameters are defined in ``config/config.json``, a table schema will be created within the
first request to the connector. A file ``{connector_dir}/installer.lock`` will be created then, to avoid the second execution of ``schema.sql``.

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS `mapping`
    (
        `endpoint` VARBINARY(32) NOT NULL,
        `host`     INT        NOT NULL,
        `type`     INT        NOT NULL,
        PRIMARY KEY (`endpoint`, `type`)
    );

    CREATE TABLE IF NOT EXISTS `categories`
    (
        `id`        VARBINARY(32) NOT NULL,
        `parent_id` VARBINARY(32) NULL,
        `status`    TINYINT    NOT NULL,
        PRIMARY KEY (`id`)
    );

    CREATE TABLE IF NOT EXISTS `category_translations`
    (
        `category_id`      VARBINARY(32)   NOT NULL,
        `language_iso`     VARCHAR(2)   NOT NULL,
        `name`             VARCHAR(255) NOT NULL,
        `description`      TEXT         NULL,
        `title_tag`        VARCHAR(255) NULL,
        `meta_description` VARCHAR(255) NULL,
        `meta_keywords`    VARCHAR(255) NULL,
        PRIMARY KEY (`category_id`, `language_iso`),
        FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
    );
