from pprint import pprint

from PyInstaller.compat import getenv
from dotenv import load_dotenv
import os
import requests
load_dotenv('../../.env')

city = input("Enter city name: ")

address = f"https://api.weatherapi.com/v1/current.json?key={os.getenv('WHEATHERAPI_KEY')}&q=London&aqi=no"


response = requests.get(address)

print(response.json()['current']['temp_c'])
