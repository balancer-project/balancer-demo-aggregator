import logging

g_logging_level = logging.INFO

g_http_port = 49172

g_banking_connector_url = "http://localhost:49162"

g_core_db_config = {
    "host": "localhost",
    "dbname": "core-db",
    "port": 49153,
    "user": "core",
    "password": "local-dev"
}

g_banking_connector_db_config = {
    "host": "localhost",
    "dbname": "banking-connector-db",
    "port": 49163,
    "user": "banking-connector",
    "password": "local-dev"
}
