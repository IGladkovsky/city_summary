import clients.rates
import clients.weather


def is_warm_clothes_needed(city) -> dict:
    wmo_weather_codes = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "fog",
        48: "depositing rime fog",
        51: "light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",
        56: "light freezing drizzle",
        57: "dense freezing drizzle",
        61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",
        66: "light freezing rain",
        67: "heavy freezing rain",
        71: "slight snow fall",
        73: "moderate snow fall",
        75: "heavy snow fall",
        77: "snow grains",
        80: "slight rain showers",
        81: "moderate rain showers",
        82: "violent rain showers",
        85: "slight snow showers",
        86: "heavy snow showers",
        95: "thunderstorm",
        96: "thunderstorm with slight hail",
        99: "thunderstorm with heavy hail",
    }
    data = clients.weather.get_weather(city)
    data_to_return = {
        "city": data["city"],
        "weather": {
            "temp_c": data["temp_c"],
            "description": wmo_weather_codes.get(data["weather_code"], "unknown"),
            "warm_clothes": data["temp_c"] < 0,
        },
    }
    return data_to_return


def is_rate_expensive(currency) -> dict:
    rate = clients.rates.get_rate(currency)
    is_expensive = rate > 100
    data = {
        "currency": currency.upper(),
        "rates_to_rub": rate,
        "expensive": is_expensive,
    }
    return data
