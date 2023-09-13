from asyncio.log import logger

import requests as requests

from config.config import g_banking_connector_url


def call_webhook_for_onetime() -> None:
    body = {
        "webhook_type": "TRANSACTIONS",
        "webhook_code": "SYNC_UPDATES_AVAILABLE",
        "item_id": "P6yK7VJdMvFbK6xrpgzms9BEo547ZZI7VKxW8",
        "initial_update_complete": True,
        "historical_update_complete": True,
        "environment": "sandbox"
    }

    logger.info("Calling SYNC_UPDATES_AVAILABLE webhook for a one-time-expense-related transaction")

    requests.post(
        url=g_banking_connector_url + "/v1/bank-link/notify-update",
        json=body
    )
