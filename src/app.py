from asyncio.log import logger

import psycopg2
from flask import Flask

from config.config import g_http_port, g_core_db_config, g_banking_connector_db_config

g_welcome_ascii_art = '''
┌┐ ┌─┐┬  ┌─┐┌┐┌┌─┐┌─┐┬─┐
├┴┐├─┤│  ├─┤││││  ├┤ ├┬┘
└─┘┴ ┴┴─┘┴ ┴┘└┘└─┘└─┘┴└─
Demo banking aggregator
Balancer project by Juan Carrion
'''


class App:

    instance = None
    flask_instance = None
    core_db_connection = None
    banking_connector_db_connection = None
    transactions = []

    @staticmethod
    def print_welcome() -> None:
        logger.info(g_welcome_ascii_art)

    @staticmethod
    def init() -> None:
        if App.instance is not None:
            raise RuntimeError('App has already been initialized.')

        App.instance = App()

        App.flask_instance = Flask(
            __name__,
            static_folder="../resources/static",
            template_folder="../resources/templates"
        )

        # noinspection PyUnresolvedReferences
        import src.routes

        App.core_db_connection = psycopg2.connect(
            host=g_core_db_config["host"],
            dbname=g_core_db_config["dbname"],
            port=g_core_db_config["port"],
            user=g_core_db_config["user"],
            password=g_core_db_config["password"]
        )

        App.banking_connector_db_connection = psycopg2.connect(
            host=g_banking_connector_db_config["host"],
            dbname=g_banking_connector_db_config["dbname"],
            port=g_banking_connector_db_config["port"],
            user=g_banking_connector_db_config["user"],
            password=g_banking_connector_db_config["password"]
        )

    @staticmethod
    def terminate() -> None:
        logger.info("Closing connections and exiting...")

        App.core_db_connection.close()
        App.banking_connector_db_connection.close()

    @staticmethod
    def run() -> None:
        App.init()
        App.print_welcome()
        App.flask_instance.run(port=g_http_port)
