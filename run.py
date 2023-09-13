import atexit
import logging

from config.config import g_logging_level
from src.app import App

if __name__ == '__main__':
    logging.basicConfig(level=g_logging_level)

    App.run()

atexit.register(App.terminate)
