from asyncio.log import logger

from src.app import App


def initialize_demo_data() -> None:
    with App.core_db_connection.cursor() as core_cursor, \
            App.banking_connector_db_connection.cursor() as banking_connector_cursor:
        logger.info("Initializing data at Core microservice")

        with open("resources/sql/core-initialize.sql") as sql:
            core_cursor.execute(sql.read())

        logger.info("Initializing data at banking connector microservice")

        with open("resources/sql/banking-connector-initialize.sql") as sql:
            banking_connector_cursor.execute(sql.read())

        App.core_db_connection.commit()
        App.banking_connector_db_connection.commit()
