.. index::
   single: Process

Process
=======

**The Wawi expects an Id that my models do not have. What should I do?**

**Where is the edit action?**

**Which data is required to be existent in the endpoint?**

Basically the same data you have in your Wawi.
* At least one customer group
* The same tax rates in endpoint and Wawi
* At least one language which exists in the Wawi as well
* At least one currency which exists in the Wawi as well

**How is it ensured that the Id of a newly created entity can be used in the same process?**

The data is pushed by the Wawi in a way that the id of newly created models in the endpoint can be used by
other models referring to it. This means e.g. that categories are pushed before products, before images.

Identity Linking
----------------

**At which point does the linking happen?**



**What does it mean if the Host/Endpoint is set or empty?**

===== ======== ===========
Host  Endpoint Action
===== ======== ===========
False True     Pull
True  False    Push
True  True     Delete/Push
===== ======== ===========

**What do I need for linking?**

The linking has to be stored in a mapping table. Reference?