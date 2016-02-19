from django.test import TestCase
from services import getCurrentWeather

# Create your tests here.
class WeatherTestCase(TestCase):

    def testRequestWeatherApi(self):
        json = getCurrentWeather('sao paulo')