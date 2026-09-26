import processing.preprocessing


def build_city_summary(city, currency="USD") -> dict:
    weather_data = processing.preprocessing.is_warm_clothes_needed(city)
    currency_data = processing.preprocessing.is_rate_expensive(currency)
    data_to_return = {
        "city": weather_data["city"],
        "weather": weather_data["weather"],
        "rates": currency_data,
    }
    return data_to_return
