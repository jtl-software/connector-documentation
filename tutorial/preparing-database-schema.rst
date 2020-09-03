Preparing database schema
=========================

Example connector needs a place to store data that we send. In this case we will use MySQL as database and file that
already contains ready to use schema ``scripts/schema.sql``.

Assuming that you have correct database connection parameters in ``config/config.json`` table schema will be created at
first call to the connector. Then lock file will be created in ``CONNECTOR_DIR`` to avoid second execution of ``schema.sql``.