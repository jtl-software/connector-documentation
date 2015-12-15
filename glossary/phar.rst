.. index::
   single: Phar

Phar
====

Phar is an extension that allows developers to combine a whole PHP application, distributed over several files, into a single one.
This file is a phar archive. The benefit of just having a single file is the easier distribution of the application.
There is no unpacking needed to run the application.
It can either be started from a webserver by including it or running it from command line.

Like any other php files the phar's combined files can also be included.

.. code-block:: php

   include 'phar:///path/to/myphar.phar/file.php';
