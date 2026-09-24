from clients.http import CurrencyNotFoundError, make_get_request


def get_rate(currency: str = "USD") -> float:
    url = f"https://api.frankfurter.dev/v2/rate/{currency}/RUB"
    response = make_get_request(url)
    if response.status_code == 422 or response.status_code == 404:
        raise CurrencyNotFoundError("Код валюты не найден")
    try:
        data = response.json()
    except ValueError:
        raise ValueError("Неверный формат или неправильный JSON")

    return data["rate"]
