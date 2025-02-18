import os
import requests


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    URL = "http://api.weatherapi.com/v1/current.json"
    key = os.environ["API_KEY"]
    city = "Paris"

    request_url = f"{URL}?key={key}&q={city}"

    response = requests.get(request_url).json()

    message = (
        f"{response["location"]["name"]}/{response["location"]["country"]} "
        f"{response["location"]["localtime"]} Weather: "
        f"{response["current"]["temp_c"]} Celsius, "
        f"{response["current"]["condition"]["text"]}"
    )

    print(message)


if __name__ == "__main__":
    get_weather()
