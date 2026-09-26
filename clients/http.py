import time

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout


class CityNotFoundError(Exception):
    pass


class CurrencyNotFoundError(Exception):
    pass


class ServiceUnavailableError(Exception):
    pass


def make_get_request(
    url: str, params: dict | None = None, timeout: int = 10, max_retries: int = 2
) -> requests.Response:
    for attempt in range(max_retries + 1):
        try:
            response = requests.get(url, params=params, timeout=timeout)

            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 5))
                time.sleep(retry_after)
                continue

            if 500 <= response.status_code < 600:
                response.raise_for_status()

            return response

        except (Timeout, ConnectionError):
            if attempt < max_retries:
                time.sleep(1)
                continue

        except HTTPError:
            if attempt < max_retries:
                time.sleep(1)
                continue

    raise ServiceUnavailableError("Внешний сервис недоступен")
