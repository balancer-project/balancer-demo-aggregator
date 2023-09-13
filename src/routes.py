from flask import request, render_template

from src.app import App
from src.demodata.initialize_demo_data import initialize_demo_data
from src.plaid.answer_to_transactions_sync import answer_to_transactions_sync
from src.plaid.call_webhook_for_one_time import call_webhook_for_onetime
from src.plaid.call_webhook_for_recurring import call_webhook_for_recurring


@App.flask_instance.route("/")
def _root():
    return render_template("panel.html")


@App.flask_instance.route("/simulator-api/demo-data", methods=["POST"])
def _initialize_demo_data() -> tuple[str, int]:
    initialize_demo_data()
    return "", 204


@App.flask_instance.route("/simulator-api/transactions/for-one-time-expense", methods=["POST"])
def _add_transaction_for_one_time_expense() -> tuple[str, int]:
    call_webhook_for_onetime()
    return "", 204


@App.flask_instance.route("/simulator-api/transactions/for-recurring-expense", methods=["POST"])
def _add_transaction_for_recurring_expense() -> tuple[str, int]:
    call_webhook_for_recurring()
    return "", 204


@App.flask_instance.route("/transactions/sync", methods=["POST"])
def _plaid_transactions_sync():
    return answer_to_transactions_sync(request)
