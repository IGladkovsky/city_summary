import argparse
import sys

import processing.service
from clients.http import (
    CityNotFoundError,
    CurrencyNotFoundError,
    ServiceUnavailableError,
)


def main() -> None:
    try:
        parser = argparse.ArgumentParser(exit_on_error=False)
        parser.add_argument("--city", type=str, required=True)
        parser.add_argument("--currency", type=str, default="USD")
        args = parser.parse_args()
        data = processing.service.build_city_summary(args.city, args.currency)
        print(
            f"Город: {data['city']}\n"
            f"Погода: {data['weather']['temp_c']}°C, {data['weather']['description']}\n"
            f"Тёплая одежда: {'да' if data['weather']['warm_clothes'] else 'нет'}\n"
            f"{args.currency.upper()}→RUB: {data['rates']['rates_to_rub']}\n"
            f"Дорогой курс: {'да' if data['rates']['expensive'] else 'нет'}"
        )

    except argparse.ArgumentError as e:
        print(e)
        sys.exit(2)
    except (
        ValueError,
        CityNotFoundError,
        CurrencyNotFoundError,
        TypeError,
    ) as e:
        print(e)
        sys.exit(3)
    except ServiceUnavailableError as e:
        print(e)
        sys.exit(4)
    sys.exit(0)


if __name__ == "__main__":
    main()
