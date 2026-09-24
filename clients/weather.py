from clients.http import CityNotFoundError, make_get_request


def get_weather(city: str) -> dict:
    geo_response = make_get_request(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "en", "format": "json"},
    )
    try:
        geo_data = geo_response.json()
    except ValueError:
        raise ValueError("Неверный формат или неправильный JSON")
    if not geo_data.get("results"):
        raise CityNotFoundError("Город не найден")

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    weather_response = make_get_request(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code",
            "timezone": "auto",
        },
    )
    try:
        weather_data = weather_response.json()
    except ValueError:
        raise ValueError("Неверный формат или неправильный JSON")

    return weather_data
