from datetime import date

from flask import Request

g_today = date.today().strftime("%Y-%m-%d")

g_one_time_cursor = \
    "ktyj7LNeuDQV9DzkGdyhAFqbpLS9Z7kLH25aMnpx8NRBCcpjwRruVmDckzHBpmhS3YBXAkBq3y38KJtCjVBNMxDFgmFindCmyYDYUujzUdj4zWPQ"
g_recurring_cursor = \
    "cQWH3qT87Wu8yibBbfPLav35GZPdxzjGca2D9zF9xbnBaBA3f19cXJEBbYPWgCvFPx48DZP4YKQp06CJBZqRqESgJpBgPuJ0DXNERzkr6UNjVa5t"
g_last_cursor = \
    "aB3BAALE9dcv9v9By7CMVVeCzJ54VL1qxkTTkdWMT55f1M9DG42d838jS7Pvjz8rdr1UtXvHmUfGKtFfJXj3rifuDgpnjDF1vh8NaC7PzMVEPVYM"

g_one_time_sync_result = {
    "added": [
        {
            "account_id": "BxBXxLj1m4HMXBm9WZZmCWVbPjX16EHwv99vp",
            "amount": 70.00,
            "iso_currency_code": "EUR",
            # "unofficial_currency_code": None,
            "category": [],
            "category_id": "19013000",
            # "check_number": None,
            "date": g_today,
            # "datetime": None,
            # "authorized_date": None,
            # "authorized_datetime": None,
            # "location": None,
            "name": "Renfe",
            "merchant_name": "Renfe",
            # "payment_meta": None,
            "payment_channel": "online",
            "pending": False,
            # "pending_transaction_id": None,
            "personal_finance_category": {
                "primary": "TRAVEL",
                "detailed": "TRAVEL_OTHER_TRAVEL"
            },
            # "account_owner": None,
            "transaction_id": "SFASHdQdAc9BVU8vKA3j8N7ChSz0u4SibkkVK",
            # "transaction_code": None,
        }
    ],
    "modified": [],
    "removed": [],
    "next_cursor": g_recurring_cursor,
    "has_more": False,
    "request_id": "YFnbf"
}

g_recurring_sync_result = {
    "added": [
        {
            "account_id": "BxBXxLj1m4HMXBm9WZZmCWVbPjX16EHwv99vp",
            "amount": 700.00,
            "iso_currency_code": "EUR",
            # "unofficial_currency_code": None,
            "category": [],
            "category_id": "19013000",
            # "check_number": None,
            "date": g_today,
            # "datetime": None,
            # "authorized_date": None,
            # "authorized_datetime": None,
            # "location": None,
            "name": "Cobro renta septiembre 2023 alquiler calle Marsha P. Johson",
            "merchant_name": "Inmobiliaria",
            # "payment_meta": None,
            "payment_channel": "online",
            "pending": False,
            # "pending_transaction_id": None,
            "personal_finance_category": {
                "primary": "RENT_AND_UTILITIES",
                "detailed": "RENT_AND_UTILITIES_RENT"
            },
            # "account_owner": None,
            "transaction_id": "SRci6nQHduDLnFedifAMk3w4WqnEpNGENht5a",
            "transaction_code": "direct debit"
        }
    ],
    "modified": [],
    "removed": [],
    "next_cursor": g_last_cursor,
    "has_more": False,
    "request_id": "YFnbf"
}


def answer_to_transactions_sync(request: Request) -> dict:
    if request.json["cursor"] == g_one_time_cursor:
        return g_one_time_sync_result

    if request.json["cursor"] == g_recurring_cursor:
        return g_recurring_sync_result

    return {}
