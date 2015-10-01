Token loader
============

JTL-Connector uses an **authorization token** to authenticate clients and authorize access to the endpoint.
This token is entered as synchronization password inside JTL-Wawi.
As JTL-Connector strives to be as flexible as possible it does not enforce a certain procedure on how to store this password.
It thus delegates this task to the endpoint, communicating via an object of interface `jtl\\Connector\\Authentication\\ITokenLoader <https://gitlab.jtl-software.de/jtl-software-gmbh/jtlconnector/blob/master/src/jtl/Connector/Authentication/ITokenLoader.php>`_.

This interface has only one method `load()` that returns the correct auth token for the endpoint.

.. note::
    You are free to store this token wherever you want, be it a settings subsystem available in the targeted shop or a simple plain file.
    However, if there is any possibility to access backend configuration settings from your endpoint we recommend that you use the shop's standard facilities to store the token.
    This ensures that your users can freely renew the token if they want to.

The example connector returns a hardcoded token.
This approach is generally **strongly discouraged** but was chosen here for the purpose of demonstration.
Remember that this token must be considered as a password.
You should choose a *secure storage* and ideally use encryption if your target system supports it.
