Category controller
===================

The Category controller is one of the main controllers. Others for example are Product, Manufacturer, Customer, CustomerOrder etc. You can find them in :ref:`data models <data-models>`.

.. note::
    You can read more about the request flow here: :ref:`fundamentals`

The implementation of the Category controller in the example contains all basic methods that can be called:

- statistic
- pull
- push
- delete

.. note::
    We decided to use `UUID's <https://de.wikipedia.org/wiki/Globally_Unique_Identifier>`_ for creating
    ids in the (example) shop inside the example connector. However, it depends on the platform you want to connect with JTL-Wawi what type of ids are present. Please also see how the :ref:`primary-key-mapper` works.

Here is a json payload example, that you can send to the endpoint (e.g. by using the :ref:`connector tester <debugging-client-side>`) for creating a new category with two translations:

.. code-block:: json

    [
      {
        "attributes": [],
        "customerGroups": [],
        "i18ns": [
          {
            "categoryId": [
              "",
              1
            ],
            "languageISO": "ger",
            "name": "Katalog #1",
            "description": "",
            "urlPath": "",
            "metaDescription": "",
            "titleTag": "",
            "metaKeywords": ""
          },
          {
            "categoryId": [
              "",
              1
            ],
            "languageISO": "eng",
            "name": "Catalogue #1",
            "description": "",
            "urlPath": "",
            "metaDescription": "",
            "titleTag": "",
            "metaKeywords": ""
          }
        ],
        "invisibilities": [],
        "level": 0,
        "entityType": "Category",
        "id": [
          "",
          1
        ],
        "parentCategoryId": [
          "",
          0
        ],
        "isActive": true,
        "sort": 0
      }
    ]

AbstractController.php file

.. code-block:: php

    <?php

    namespace Jtl\Connector\Example\Controller;

    use PDO;

    /**
     * Abstract controller class to pass the database object only once.
     *
     * Class AbstractController
     * @package Jtl\Connector\Example\Controller
     */
    abstract class AbstractController
    {
        /**
         * @var PDO
         */
        protected $pdo;

        /**
         * Using direct dependencies for better testing and easier use with a DI container.
         *
         * AbstractController constructor.
         * @param PDO $pdo
         */
        public function __construct(PDO $pdo)
        {
            $this->pdo = $pdo;
        }
    }

CategoryController.php file

.. code-block:: php

    <?php

    namespace Jtl\Connector\Example\Controller;

    use Jtl\Connector\Core\Controller\DeleteInterface;
    use Jtl\Connector\Core\Controller\PullInterface;
    use Jtl\Connector\Core\Controller\PushInterface;
    use Jtl\Connector\Core\Controller\StatisticInterface;
    use Jtl\Connector\Core\Definition\IdentityType;
    use Jtl\Connector\Core\Model\AbstractDataModel;
    use Jtl\Connector\Core\Model\Category;
    use Jtl\Connector\Core\Model\CategoryI18n;
    use Jtl\Connector\Core\Model\Identity;
    use Jtl\Connector\Core\Model\QueryFilter;
    use Ramsey\Uuid\Uuid;

    /**
     * Creating the controller for the entity that the controller should support using the method interfaced to define supported methods
     *
     * Class CategoryController
     * @package Jtl\Connector\Example\Controller
     */
    class CategoryController extends AbstractController implements PullInterface, PushInterface, StatisticInterface, DeleteInterface
    {
        /**
         * @param AbstractDataModel $model
         * @return AbstractDataModel
         */
        public function delete(AbstractDataModel $model): AbstractDataModel
        {
            /** @var $model Category */
            if (!empty($categoryId = $model->getId()->getEndpoint())) {
                $statement = $this->pdo->prepare("DELETE FROM categories WHERE id = ?");
                $statement->execute([$categoryId]);
            }

            return $model;
        }

        /**
         * @param AbstractDataModel $model
         * @return AbstractDataModel
         */
        public function push(AbstractDataModel $model): AbstractDataModel
        {
            /** @var Category $model */
            $endpointId = $model->getId()->getEndpoint();

            if (empty($endpointId)) {
                $endpointId = Uuid::uuid4()->getHex()->toString();
                $model->getId()->setEndpoint($endpointId);
            }

            $query = "INSERT INTO categories (id, parent_id, status) VALUES (?, ?, ?) ON DUPLICATE KEY UPDATE status = ?, parent_id = ?";

            $params = [
                $endpointId,
                $parentId = $model->getParentCategoryId()->getEndpoint() === '' ? null : $model->getParentCategoryId()->getEndpoint(),
                $status = (int)$model->getIsActive(),
                $status,
                $parentId
            ];

            $statement = $this->pdo->prepare($query);
            $statement->execute($params);

            foreach ($model->getI18ns() as $i18n) {
                $statement = $this->pdo->prepare(
                    "INSERT INTO category_translations (category_id, name, description, title_tag, meta_description, meta_keywords, language_iso) VALUES (?, ?, ?, ?, ?, ?, ?)
                               ON DUPLICATE KEY UPDATE name = ?, description = ?, title_tag = ? , meta_description = ?, meta_keywords = ?");

                $statement->execute([
                    $endpointId,
                    $i18n->getName(),
                    $i18n->getDescription(),
                    $i18n->getTitleTag(),
                    $i18n->getMetaDescription(),
                    $i18n->getMetaKeywords(),
                    $i18n->getLanguageIso(),
                    $i18n->getName(),
                    $i18n->getDescription(),
                    $i18n->getTitleTag(),
                    $i18n->getMetaDescription(),
                    $i18n->getMetaKeywords(),
                ]);
            }

            return $model;
        }

        /**
         * @inheritDoc
         */
        public function pull(QueryFilter $queryFilter): array
        {
            $return = [];

            $statement = $this->pdo->prepare("
                SELECT id as id, parent_id as parent_id, status FROM categories c
                LEFT JOIN mapping m ON c.id = m.endpoint
                WHERE m.host IS NULL OR m.type != ?
            ");

            $statement->execute([
                IdentityType::CATEGORY
            ]);

            $categories = $statement->fetchAll(\PDO::FETCH_ASSOC);

            foreach ($categories as $category) {
                $return[] = $this->createJtlCategory($category);
            }

            return $return;
        }

        /**
         * @param QueryFilter $queryFilter
         * @return int
         */
        public function statistic(QueryFilter $queryFilter): int
        {
            $statement = $this->pdo->prepare("
                SELECT * FROM categories c
                LEFT JOIN mapping m ON c.id = m.endpoint
                WHERE m.host IS NULL OR m.type != ?
            ");
            $statement->execute([
                IdentityType::CATEGORY
            ]);

            return $statement->rowCount();
        }

        /**
         * @param array $category
         * @return Category
         */
        protected function createJtlCategory(array $category): Category
        {
            $jtlCategory = (new Category)
                ->setId(new Identity($category['id']))
                ->setIsActive($category["status"])
                ->setParentCategoryId(new Identity($category['parent_id'] ?? ''));

            $statement = $this->pdo->prepare("
                SELECT * FROM category_translations t
                LEFT JOIN categories c ON c.id = t.category_id
                WHERE c.id = ?
            ");
            $statement->execute([$category['id']]);
            $i18ns = $statement->fetchAll(\PDO::FETCH_ASSOC);

            foreach ($i18ns as $i18n) {
                $jtlCategory->addI18n($this->createJtlCategoryI18n($i18n));
            }

            return $jtlCategory;
        }

        /**
         * @param array $i18n
         * @return CategoryI18n
         */
        protected function createJtlCategoryI18n(array $i18n): CategoryI18n
        {
            return (new CategoryI18n())
                ->setName($i18n["name"])
                ->setDescription($i18n["description"] ?? "")
                ->setTitleTag($i18n["title_tag"] ?? "")
                ->setMetaDescription($i18n["meta_description"] ?? "")
                ->setMetaKeywords($i18n["meta_keywords"] ?? "")
                ->setLanguageIso($i18n["language_iso"] ?? "");
        }
    }
