.. _token-validator:

Token validator
============

JTL-Connector uses an **authorization token** to authenticate clients and authorize access to the endpoint.
This token is entered as synchronization password inside JTL-Wawi.
As JTL-Connector strives to be as flexible as possible it does not enforce a certain procedure on how to store this password.
It thus delegates this task to the endpoint, communicating via an object of interface `Jtl\Connector\Core\Authentication\TokenValidatorInterface <https://github.com/jtl-software/connector-core/blob/develop/src/Authentication/TokenValidatorInterface.php>`_.

This interface has only one method, :code:`validate()` that returns a boolean whether the provided token is valid.

.. note::
    You are free to store this token wherever you want, be it a settings subsystem available in the targeted shop or a simple plain file.
    However, if there is any possibility to access backend configuration settings from your endpoint we recommend that you use the shop's standard facilities to store the token.
    This ensures that your users can freely renew the token if they want to.

