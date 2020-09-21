Example
=======

The location of a newly created plugin is inside the plugins folder of the connector's root directory.
The namespace of the plugins classes is based on `PSR-0 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0-autoloader.md>`_ equal to the folder path.
For this example we created a simple plugin that attaches a suffix to every category name.

.. _plugin-bootstrap:

Example plugin in connector directory structure
-----------------------------------------------
::

    connector-root
    ├── config
    ├── plugins
    │   └── DemoPlugin
    │       └── Bootstrap.php
    ├── src
    ├── other
    ├── directories
    ├── var
    └── vendor


Bootstrap.php
-------------

The following class is placed in ``{connector_dir}/plugins/DemoPlugin/Bootstrap.php``. It stays inside the namespace :code:`DemoPlugin`.
In addition to the class name ``DemoPlugin\Bootstrap`` the ``Jtl\Connector\Core\Plugin\PluginInterface`` interface has to be implemented by the class, in order to be detected by the :doc:`Core</glossary/core>`.
There is no other action needed to register the plugin.

.. code-block:: php

    <?php

    namespace DemoPlugin;

    use DI\Container;
    use Jtl\Connector\Core\Definition\Action;
    use Jtl\Connector\Core\Definition\Controller;
    use Jtl\Connector\Core\Definition\Event;
    use Jtl\Connector\Core\Event\CategoryEvent;
    use Jtl\Connector\Core\Plugin\PluginInterface;
    use Noodlehaus\ConfigInterface;
    use Symfony\Component\EventDispatcher\EventDispatcher;

    //Every plugin which occurs in the connector/plugins is registered by the connector
    class Bootstrap implements PluginInterface
    {
        //Using the registerListener function, provided by the PluginInterface to define when the plugin should call what method
        public function registerListener(ConfigInterface $config, Container $container, EventDispatcher $dispatcher)
        {
            //Using static variables to define the wanted event name which is used to determine when the plugins is called
            $eventName = Event::createEventName(
                Controller::CATEGORY,
                Action::PUSH,
                Event::BEFORE
            );

            $dispatcher->addListener($eventName, [$this, "handle"]);
        }

        public function handle(CategoryEvent $event)
        {
            foreach ($event->getCategory()->getI18ns() as $i18n) {
                $i18n->setName(sprintf("%s_suffix", $i18n->getName()));
            }
        }
    }

In the body of the :code:`registerListener()` method you have to subscribe the events you want to listen to.
The code snipped above shows adding of a category before push event. The first parameter of the :code:`addListener()` method is the name of the event you want to listen to.
The second parameter is a callable function with an event object as argument (event arg).

The event argument contains a main models object, which can be accessed by a getter.
In this case :code:`$event->getCategory()` returns the object. It can be modified in a before event or used like in this example in an after event.

That is basically all you need to know if you want to write a plugin for an :doc:`endpoint </glossary/endpoint>`.
