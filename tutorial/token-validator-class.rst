.. _token-validator-class:

Token validator class
=====================

The :ref:`token validator <token-validator>` verifies if an authorization token is valid or not.
It is responsibility of an endpoint to validate the token.

.. code-block:: php

    <?php

    namespace Jtl\Connector\Core\Authentication;

    use Jtl\Connector\Core\Exception\TokenValidatorException;

    /**
     * Class TokenValidator
     * @package Jtl\Connector\Core\Authentication
     */
    class TokenValidator implements TokenValidatorInterface
    {
        /**
         * @var string
         */
        protected $token;

        /**
         * TokenValidator constructor.
         * @param string $token
         * @throws TokenValidatorException
         */
        public function __construct(string $token)
        {
            if ($token == '') {
                throw TokenValidatorException::emptyToken();
            }
            $this->token = $token;
        }

        /**
         * @param string $token
         * @return bool
         */
        public function validate(string $token): bool
        {
            return $this->token === $token;
        }
    }
