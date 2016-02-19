# https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%20455827&format=json&env=store%3A%2F%2Fdatatables.org%2https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%20455827&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22sao%20paulo%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys

# https://query.yahooapis.com/v1/public/yql
# q = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="sao paulo")'
# format = json
# env = store%3A%2F%2Fdatatables.org%2Falltableswithkeys
import requests
from weather.serializer import WeatherSerializer


def getCurrentWeather(city):
    url = 'https://query.yahooapis.com/v1/public/yql'
    params = {'q': 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + city
                   + '")',
               'format': 'json',
               'env': 'store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
               }
    response  = requests.get(url, params=params)
    jsonResponse = response.json()
    return WeatherSerializer.create(
        humidity=jsonResponse['query']['results']['channel']['atmosphere']['humidity'],
        temperature=jsonResponse['query']['results']['channel']['item']['condition']['temp'],
        wind=jsonResponse['query']['results']['channel']['wind']['speed'],
        condition=jsonResponse['query']['results']['channel']['item']['condition']['text']
    )
