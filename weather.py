import requests as re


def fetch_weather_data(url):
    try:
        response = re.get(url, timeout=10)
        json_data = response.json()
        print("Fetched weather data successfully.")
        # print(json_data)
        return specific_weather_information(json_data)

    except Exception as error:
        print("Error fetching weather data.")
        print(str(error))
        return None


def specific_weather_information(json_data):
    try:
        if json_data is None:
            print("No JSON data found.")
            return None

        dict_data = {}
        dict_data['city'] = json_data['name']
        dict_data['temperature'] = json_data['main']['temp']
        dict_data['feels_like'] = json_data['main']['feels_like']
        dict_data['main'] = json_data['weather'][0]['main']
        dict_data['description'] = json_data['weather'][0]['description']
        dict_data['humidity'] = json_data['main']['humidity']
        dict_data['wind_speed'] = json_data['wind']['speed']

        print(dict_data)
        return dict_data

    except Exception as error:
        print("Error fetching specific weather information.")
        print(str(error))
        return None


def main():
    # This main function is for testing only
    # The API key is now handled in app.py
    print("Use app.py to run the Weather App")


if __name__ == '__main__':
    main()
