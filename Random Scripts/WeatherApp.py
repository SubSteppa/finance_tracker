# https://roadmap.sh/projects/weather-api-wrapper-service

import requests
import json

api_key = "PLNWALHQ2WUBX24A3RMVT4XUR"
location = input("Input your location here")
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={api_key}&unitGroup=metric&include=days"

try:

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if "errorCode" in data:
        print(f"Error: {data['message']}")
    else:
        today = data['days'][0]
        print(f"Weather for: {data['resolvedAddress']}")
        print(f"Temperature: {today['temp']}°C")
        print(f"Min is {today['tempmin']}°C Max {today['tempmax']}°C")

except requests.exceptions.RequestException as e:
    print("Network error: Bad API Request - Invalid location")
except (KeyError, IndexError):
    print("Could not find weather data for that location.")
