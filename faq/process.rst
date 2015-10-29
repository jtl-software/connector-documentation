Process
=======

**The Wawi expects an id that my models do not have. What should I do?**

Let us take the ``CustomerOrder`` model as an example. It has the relations ``BillingAddress`` and ``PaymentAddress``.
If one or both addresses would be stored in the same table they don't have an id.
In this case you can use the id of the order and by using a prefix or suffix building an id for the address.
For example the order id is 5 than the billing address id could be b_5 and the payment address id p_5.

**How can I differentiate between an add and edit action?**

If you are adding a new model the endpoint id cannot be mapped to the host id.
After adding a mapping is saved and the host id and endpoint id can be mapped.
This points out that an edit action should take place.

**Which data is required to be existent in the endpoint?**

Basically the same data you have in your JTL-Wawi.

* At least one customer group
* The same tax rates in endpoint and JTL-Wawi
* At least one language which exists in JTL-Wawi as well
* At least one currency which exists in JTL-Wawi as well

**How is it ensured that the Id of a newly created entity can be used in the same process?**

The data is pushed by JTL-Wawi in a way that the id of newly created models in the endpoint can be used by
other models referring to it. This means e.g. that categories are pushed before products, before images.

Identity Linking
----------------

.. **At which point does the linking happen?**

**What does it mean if the Host/Endpoint is set or empty?**

===== ======== ===========
Host  Endpoint Action
===== ======== ===========
False True     Pull
True  False    Push
True  True     Delete/Push
===== ======== ===========

**What do I need for linking?**

The linking has to be stored in a mapping table, see :ref:`primary-key-mapper`.