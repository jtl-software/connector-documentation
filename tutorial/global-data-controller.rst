GlobalData controller
=====================

GlobalData controller is responsible for returning 'global' information about endpoint configuration like available
languages, currencies, customer groups etc. You can find full list of possible info that can be set inside ``Jtl\Connector\Core\Model\GlobalData``
model class.

In example connector we will use hardcoded values only for presentation. Real implementation should get actual values
and return them to client.