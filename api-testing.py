import requests
import os
import time

city = input("Enter city name : ")

weather_api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=81d5a9e1f5052ff133a7557596cd8606"
data = requests.get(url=weather_api)
gson = data.json()
description = gson["weather"][0]["description"]
temp = gson["main"]["temp"]
humidity = gson["main"]["humidity"]
name = gson["name"]

w = "WELCOME"
st = ""
for i in w:
    os.system("clear")
    st = st + i
    print(st)
    time.sleep(.3)

time.sleep(.3)
print("#"*50)
time.sleep(.3)
print(f"#{name:^48}#")
time.sleep(.3)
print("#"*50)
time.sleep(.3)
print(f"# Description | {description:>32} #")
time.sleep(.3)
print(f"# Temperature | {temp:>32} #")
time.sleep(.3)
print(f"# Humidity    | {humidity:>32} #")
time.sleep(.3)
print("#"*50)
print()
print()
print()
print()
