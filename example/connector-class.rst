Connector class
===============

JTL-Connector makes use of an RPC-style communication protocol together with JTL-Wawi.
To write a full-featured endpoint implementation you do not have to know any detail on how this has been implemented.
At the moment it is enough to say that this protocol provides method call semantics to your endpoint, i.e. you provide methods, grouped into several RPC objects, that can be called from the client.
Those methods, of course, can have parameters.

All details of the communication, protocol decoding and verifications are abstracted away by :doc:`jtlconnector </glossary/jtlconnector>`.
The main hub for all valid requests is the **Connector** class whose job is to pass RPC calls to the respective controllers as well as to provide the application with certain definitions.

The (abridged) implementation of our example endpoint looks like this:

.. code-block:: php

    <?php

    namespace Jtl\Connector\Example;

    use DI\Container;
    use Jtl\Connector\Core\Authentication\TokenValidatorInterface;
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
        protected $config;
        protected $db;

        public function initialize(ConfigInterface $config, Container $container, EventDispatcher $eventDispatcher) : void
        {
            $this->config = $config;
            $this->db = $this->getDatabaseInstance();

            //Checks if the connector-token is set to control if the installing routine should be executed
            if (!$this->config->has("token")) {
                $installer = new Installer($this->db);
                $installer->run();

                $this->config->set("token", "123456789");
                $this->config->write();
            }

            //Passing the instantiated database object the the DI container so it can later be accessed by the controllers
            $container->set(PDO::class, $this->db);
        }

        public function getPrimaryKeyMapper() : PrimaryKeyMapperInterface
        {
            //Defining the PrimaryKeyMapper which is used to manage the links between WAWI and shop entities
            return new PrimaryKeyMapper($this->db);
        }

        public function getTokenValidator() : TokenValidatorInterface
        {
            //Defining the TokenValidator which is used to check the given token on an Auth call
            return new TokenValidator($this->config);
        }

        public function getControllerNamespace() : string
        {
            //Defining the ControllerNamespace which holds the controller classes for all entities so the can be found by the application
            return "Jtl\Connector\Example\Controller";
        }

        public function getEndpointVersion() : string
        {
            //Defining the connectors associated shop version
            return "0.1";
        }

        public function getPlatformVersion() : string
        {
            //Defining the connectors version
            return "1";
        }

        public function getPlatformName() : string
        {
            //Defining the connectors associated shop name using "Bulk" as the default name for all test-connectors
            return "Bulk";
        }

        private function getDatabaseInstance() : PDO
        {
            $dbParams = $this->config->get("db");

            $db = new PDO(
                sprintf("mysql:host=%s;dbname=%s", $dbParams["host"], "example_connector_db"),
                $dbParams["username"],
                $dbParams["password"]/*,
                [PDO::ERRMODE_EXCEPTION]*/
            );
            $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            return $db;
        }
    }

The :code:`Connector` class implements an interface base provided by :doc:`jtlconnector </glossary/jtlconnector>` to ensure that all mandatory methods are defined.
One of those methods is the :code:`initialize` method which is executed each time the connector is used. We use this method to instantiate or save any object that will be needed in following classes. The intended way to open access to those objects is by registering them in the DI container.
In this example we also the this method to call an installer class which then sets up any needed tables and writes the connector token the the config file.
The connector class is also used to define specific classes like the PrimaryKeyMapper and the TokenValidator.
The use of those classes will be explained later on.
