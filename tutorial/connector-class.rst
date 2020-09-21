.. _connector-class:

Connector class
===============

JTL-Connector makes use of a communication protocol in RPC-style.
To write a full-featured endpoint implementation, you do not have to know any detail on how this has been implemented.
It is enough to say that this protocol provides method call semantics to your endpoint, i.e. you provide methods, grouped into several RPC objects, that can be called from the client (JTL-Wawi mostly).
Those methods, of course, can have parameters.

All details of the communication, protocol decoding and verifications are abstracted away by :doc:`Core</glossary/core>`.
The main hub for all valid requests is the **Jtl\\Connector\\Core\\Application\\Application** class, whose job is to pass RPC calls to the respective controllers. It is depending on an instance of a class which has implemented the **Jtl\\Connector\\Core\\Connector\\ConnectorInterface** interface, to initialize the endpoint environment.

The :code:`Connector` class implements an interface base provided by the :doc:`Core</glossary/core>` to ensure that all mandatory methods are defined.
One of those methods is the :code:`initialize` method which is executed each time the connector is called. This method can be used to instantiate or save any object that will be needed in following classes. The intended way to open access to those objects is by registering them in the DI container.
In this example we also use the this method to call an installer class which then sets up any needed tables and writes the connector token the the config file.
The connector class is also used to define specific classes like the PrimaryKeyMapper and the TokenValidator.
The use of those classes will be explained later on.

The implementation of the connector class from our example connector looks like the following:

.. code-block:: php

    <?php

    namespace Jtl\Connector\Example;

    use DI\Container;
    use Jtl\Connector\Core\Authentication\TokenValidatorInterface;
    use Jtl\Connector\Core\Config\ConfigSchema;
    use Jtl\Connector\Core\Connector\ConnectorInterface;
    use Jtl\Connector\Core\Mapper\PrimaryKeyMapperInterface;
    use Jtl\Connector\Example\Authentication\TokenValidator;
    use Jtl\Connector\Example\Installer\Installer;
    use Jtl\Connector\Example\Mapper\PrimaryKeyMapper;
    use Noodlehaus\ConfigInterface;
    use PDO;
    use Symfony\Component\EventDispatcher\EventDispatcher;

    /**
     * Example Connector
     * @access public
     */
    class Connector implements ConnectorInterface
    {
        public const
            INSTALLER_LOCK_FILE = 'installer.lock';
        /**
         * @var ConfigInterface
         */
        protected $config;

        /**
         * @var PDO
         */
        protected $pdo;

        /**
         * @param ConfigInterface $config
         * @param Container $container
         * @param EventDispatcher $dispatcher
         */
        public function initialize(ConfigInterface $config, Container $container, EventDispatcher $dispatcher) : void
        {
            $this->config = $config;
            $this->pdo = $this->createPdoInstance($config->get('db'));

            $connectorDir = $config->get(ConfigSchema::CONNECTOR_DIR);
            $lockFile = sprintf('%s/%s', $connectorDir, self::INSTALLER_LOCK_FILE);
            if (!is_file($lockFile)) {
                $installer = new Installer($this->pdo, $connectorDir);
                $installer->run();
                file_put_contents($lockFile, sprintf('Created at %s', (new \DateTimeImmutable())->format('Y-m-d H:i:s')));
            }

            // Passing the instantiated database object to the DI container,
            // so it can be injected into the controllers by instantiation.
            // For more information about the di container see https://php-di.org/doc/
            $container->set(PDO::class, $this->pdo);
        }

        /**
         * Defining the primary key mapper which is used to manage the links between JTL-Wawi and the shop entities.
         *
         * @return PrimaryKeyMapperInterface
         */
        public function getPrimaryKeyMapper() : PrimaryKeyMapperInterface
        {
            return new PrimaryKeyMapper($this->pdo);
        }

        /**
         * Defining the token validator which is used to check the given token on an auth call.
         *
         * @return TokenValidatorInterface
         * @throws \Exception
         */
        public function getTokenValidator() : TokenValidatorInterface
        {
            return new TokenValidator($this->config->get("token"));
        }

        /**
         * Defining the controller namespace which holds the controller classes for all entities, so they can be found by the application.
         *
         * @return string
         */
        public function getControllerNamespace() : string
        {
            return "Jtl\Connector\Example\Controller";
        }

        /**
         * Defining the connectors version.
         *
         * @return string
         */
        public function getEndpointVersion() : string
        {
            return "0.1";
        }

        /**
         * Defining the connectors associated shop version. Should be empty for "Bulk" platform.
         *
         * @return string
         */
        public function getPlatformVersion() : string
        {
            return "";
        }

        /**
         * Defining the connectors associated shop name. Using "Bulk" as the default name for all third party connectors.
         *
         * @return string
         */
        public function getPlatformName() : string
        {
            return "Bulk";
        }

        /**
         * @param string[] $dbParams
         * @return PDO
         */
        private function createPdoInstance(array $dbParams) : PDO
        {
            $pdo = new PDO(
                sprintf("mysql:host=%s;dbname=%s", $dbParams["host"], $dbParams["name"]),
                $dbParams["username"],
                $dbParams["password"]
            );

            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            return $pdo;
        }
    }

