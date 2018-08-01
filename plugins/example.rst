Example
=======

The location of a newly created plugin is inside the plugins folder of the connector's root directory.
The namespace of the plugins classes is based on `PSR-0 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0-autoloader.md>`_ equal to the folder path.
For this example we take Shopware as the shop we want to write a plugin for.

.. _plugin-bootstrap:

bootstrap.php
-------------

The following :code:`Bootstrap` class is placed in the folder plugins/izzle/demo and therefore has the namespace izzle\demo.
Regarding to the `PSR-4 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md>`_ standard the entry point of the plugin has to be called bootstrap.
In addition to the name the :code:`IPlugin` interface has to be implemented in order to be detected by the Connector-Core autoloader.
There is no other action needed to register the plugin.

.. code-block:: php

    namespace izzle\demo;

    use \jtl\Connector\Plugin\IPlugin;
    use \Symfony\Component\EventDispatcher\EventDispatcher;
    use \izzle\demo\listener\ProductListener;
    use \jtl\Connector\Event\Product\ProductAfterPushEvent;

    class Bootstrap implements IPlugin
    {
        public function registerListener(EventDispatcher $dispatcher)
        {
            $dispatcher->addListener(ProductAfterPushEvent::EVENT_NAME, [
                new ProductListener(),
                'onProductAfterPushAction'
            ]));
        }
    }

In the body of the :code:`registerListener(EventDispatcher $dispatcher)` method you have to subscribe the events you want to listen to.
The code snipped above shows the adding of a product after push event. This is the first parameter of the :code:`addListener()` method.
The second method is an array consisting of an instance of the class which should be notified and the name of the method which will be called.
Due to good code style we create an own class, the :code:`ProductListener` instead of using a method inside the :code:`Bootstrap` class.

ProductListener.php
-------------------

Like mentioned above it is recommended to create own listener classes.
Besides the coding style it will get very important if you don't have just one event you want to listen but eight up to ten on several main objects.
In our example the :code:`ProductListener` class is located in a separated folder for listeners.
As defined in our :code:`bootstrap.php` the :code:`onProductAfterPushAction` method will be called by the dispatcher after the product push.

The passed parameter contains an event. Via a getter method you have access to the main entity of the event.
In this case :code:`$event->getProduct()` returns the object. It can be modified in a before event or used like in this example in an after event.

.. code-block:: php

    namespace izzle\demo\listener;

    use \jtl\Connector\Event\Product\ProductAfterPushEvent;
    use \jtl\Connector\Shopware\Utilities\IdConcatenator;
    use \jtl\Connector\Core\Logger\Logger;
    use \jtl\Connector\Formatter\ExceptionFormatter;
    use \jtl\Connector\Core\Utilities\Language as LanguageUtil;

    class ProductListener
    {
        public function onProductAfterPushAction(ProductAfterPushEvent $event)
        {
            if (strlen($event->getProduct()->getId()->getEndpoint()) == 0) {
                return;
            }

            try {
                foreach ($event->getProduct()->getAttributes() as $attribute) {
                    foreach ($attribute->getI18ns() as $i18n) {
                        if ($i18n->getLanguageISO() === LanguageUtil::map(Shopware()->Shop()->getLocale()->getLocale())
                            && $i18n->getName() === 'maximumOrderQuantity') {

                            list($detailId, $productId) = IdConcatenator::unlink($event->getProduct()->getId()->getEndpoint());

                            $detailSW = Shopware()->Models()->find('Shopware\Models\Article\Detail', $detailId);
                            if ($detailSW !== null) {
                                $detailSW->setMaxPurchase((int) $i18n->getValue());

                                Shopware()->Models()->persist($detailSW);
                                Shopware()->Models()->flush($detailSW);
                            }
                            break;
                        }
                    }
                }
            } catch (\Exception $e) {
                Logger::write(ExceptionFormatter::format($e), Logger::WARNING, 'plugin');
            }
        }
    }

The goal of the Plugin is to support a maximum order quantity.
It is supported in Shopware by default but not in :doc:`JTL-Wawi </glossary/jtl-wawi>`.
An attribute with the name 'maximumOrderQuantity' is taken to set the value of the article details.

That is basically all you need to know if you want to extend the :doc:`Endpoint </glossary/endpoint>` with a plugin.
