#Estrutura de pasta

```
/airflow_project
├── dags/                        # Directory for all DAG definitions
│   ├── sales/                   # Sales-specific DAGs
│   │   ├── sales_pipeline_dag.py
│   │   ├── customer_report_dag.py
│   │   └── ...
│   ├── marketing/               # Marketing-specific DAGs
│   │   ├── campaign_dag.py
│   │   └── ...
│   ├── finance/                 # Finance-specific DAGs
│   │   ├── invoice_processing_dag.py
│   │   └── ...
│   └── shared/                  # Shared or reusable logic (e.g., common ETL)
│       ├── common_etl_dag.py
│       └── data_quality_dag.py
├── src/                         # Business logic and utility modules
│   ├── sales/                   # Business logic specific to sales
│   │   ├── sales_logic.py       # Sales-specific business logic
│   │   └── ...
│   ├── marketing/               # Business logic specific to marketing
│   │   ├── marketing_logic.py   # Marketing-specific business logic
│   │   └── ...
│   ├── finance/                 # Business logic specific to finance
│   │   ├── finance_logic.py     # Finance-specific business logic
│   │   └── ...
│   ├── utils/                   # Shared utility functions
│   │   ├── logging.py           # Logging utility functions
│   │   ├── data_transform.py    # Data transformation functions
│   │   └── ...
├── dbt/                        # dbt project directory
│   ├── models/                 # dbt models
│   │   ├── sales/              # Models specific to the sales domain
│   │   ├── marketing/          # Models specific to the marketing domain
│   │   ├── finance/            # Models specific to the finance domain
│   │   └── shared/             # Shared or core models
│   ├── tests/                  # dbt tests
│   ├── macros/                 # Custom dbt macros
│   ├── snapshots/              # dbt snapshots
│   ├── dbt_project.yml         # dbt project configuration
│   └── profiles.yml            # dbt connection configuration
├── astro/                      # Astro project directory
│   ├── config.yaml             # Astro project configuration
│   ├── docker-compose.override.yml # Customizations for Astro
│   ├── .astro/                 # Astro-specific files
│   └── templates/
├── config/                      # Configuration files (e.g., for connections, parameters)
│   ├── dev_config.yaml
│   ├── prod_config.yaml
│   └── staging_config.yaml
├── tests/                       # Directory for unit tests
│   ├── test_sales_logic.py      # Unit tests for sales logic
│   ├── test_marketing_logic.py  # Unit tests for marketing logic
│   ├── test_finance_logic.py    # Unit tests for finance logic
│   ├── test_logging.py          # Unit tests for logging utilities
│   └── ...
├── logs/                        # Airflow logs (auto-generated at runtime)
├── requirements.txt             # Required Python packages for the project
├── Dockerfile                   # Docker setup for Airflow (if using Docker)
└── README.md                    # Documentation about the project
```
