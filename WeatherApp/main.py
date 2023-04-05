import os

import requests
import json
import pyttsx3

engine = pyttsx3.init()

city=input("Enter the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=c0de42206f074a1ba1e145514230304&q={city}"
r= requests.get(url)
# print(r.text)
dict=json.loads(r.text)
w=dict["current"]["temp_c"]
print("Current temperature in c is:")
print(dict["current"]["temp_c"])
pyttsx3.speak("The current temp in celsius is")
pyttsx3.speak(w)
