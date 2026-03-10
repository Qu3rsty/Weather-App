# libriaries
import requests
from colorama import Fore, Style
import sys
import json
import time

# saves
with open("cities/cities.json", "r") as file:
    cities = json.load(file)

print(Fore.MAGENTA + "--- All locations ---" + Style.RESET_ALL)

for names in cities:
    print(Fore.MAGENTA + f"({cities[names]['id']}) " + Style.RESET_ALL + names)

# City search engine
CITY=input("\nSelect a town\n> ")

for name, info in cities.items():
    if str(info['id']) == CITY:
        CITY = name
        break

API_KEY="432995c174d455088bef4ec41f28dc96"
UNITS="metric"

with open("cities/cities.json", "r") as file:
    file = file.read()

url=f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}" 

response = requests.get(url)
data = response.json()

# Downloading weather data
try:
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    clouds = data['clouds']['all']
    wind_speed = data['wind']['speed'] 
except KeyError:
    print(Fore.RED + "Select the correct location!" + Style.RESET_ALL)
    sys.exit()

print(f"\n--- Weather in {CITY} ---") 

if temp > 0:
    print(Fore.YELLOW + f"- Temperature: {temp} C" + Style.RESET_ALL)
elif temp <= 0:
    print("> Temperature:", Fore.CYAN + f"{temp: .0f} C" + Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX + f"- Air humidity: {humidity}%" + Style.RESET_ALL)
print(Fore.WHITE + f"- Cloudy: {clouds}%\n" + Style.RESET_ALL)
time.sleep(5)

# Preparing more features
print(Fore.MAGENTA + "--- Next options ---" + Style.RESET_ALL)
print(Fore.MAGENTA + "(1)" + Style.RESET_ALL, "Exit")
print(Fore.MAGENTA + "(2)" + Style.RESET_ALL, "Show weather alerts")

action_2 = input("\nSelect next action\n> ")

if action_2 == '1':
    sys.exit()
elif action_2 == '2':
    print(Fore.MAGENTA + "--- Weather alerts ---" + Style.RESET_ALL)
    if temp > 30:
        print(Fore.RED + "- The temperature exceeds 30C!" + Style.RESET_ALL)
    elif temp < -5:
        print(Fore.CYAN + "- The temperature is below -5C!" + Style.RESET_ALL)
    else:
        pass
    if wind_speed > 70:
        print(Fore.RED + "- Wind speed exceeds 70km/h!" + Style.RESET_ALL)
    else:
        pass
    if not temp > 30 and not temp < -5 and not wind_speed > 70:
        print("No weather alerts :D")
    elif temp > 30 or temp < -5 and wind_speed > 70:
        print("\nYou better not leave the house today")
else:
    print(Fore.RED + "Select the correct option" + Style.RESET_ALL)
    sys.exit()