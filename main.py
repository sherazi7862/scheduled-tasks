import requests
import os
from twilio.rest import Client
url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_parameter ={
    "lat":18.988850,
    "lon":73.083138,
    "appid":my_api,
    "cnt":4,
}
data =requests.get(url,params=weather_parameter)
weather_data = data.json()
will_rain = False
for hour_data in weather_data["list"]:
    weather_code = hour_data["weather"][0]["id"]
    if weather_code <700:
        will_rain =True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring umbrella.",
        from_="+14246221138",
        to="+923347178457",
    )
print(message.status)
