# __________________________RAIN ALERT_____________________________ #
# Program looks at the weather in the user's location.
# It then texts the user whether they need an umbrella for the day.

# Import necessary libraries
import requests
from twilio.rest import Client

# Set API information
api_key = "API_KEY"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

# Set main variables
raining = False
my_lat = "LAT"
my_long = "LONG"

# Create parameters for API
parameters = {"lat": my_lat,
              "lon": my_long,
              "appid": api_key,
              "exclude": "current,minutely,daily"
              }

# Call API and store data in variable
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Slice data and check to see if it's raining
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id <= 700:
        raining = True

# Send Text message based on results of weather
if raining:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='TWILIO NUMBER',
        body="It's going to rain today! Remember to bring an umbrella!",
        to='USER NUMBER'
    )
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='TWILIO NUMBER',
        body="It's not going to rain today! No umbrella needed!",
        to='USER NUMBER'
    )
