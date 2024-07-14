import requests
from twilio.rest import Client

owm_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "560e42726d3fb2d21c436b666ca8c1bd"
Account_SID = "AC2e6d08e2e8fe466d5ba84853fa91f1f6"
Auth_Token = "b2af176d0d8cb416ae28939fc38a4418"


weather_params = {
    "lat": 26.727100,
    "lon": 88.395287,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(Account_SID, Auth_Token)
    message = client.messages.create(
        body="Its a rainy day, don't forget to bring your umbrella",
        from_='+15746867928',
        to='+917872546307'
    )
    print(message.status)



