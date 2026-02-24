# libriaries
import requests
from colorama import Fore, Style
import sys
import json

# saves
with open("cities/cities.json", "r") as file:
    cities = json.load(file)

print(Fore.MAGENTA + "--- WSZYSTKIE MIASTA ---" + Style.RESET_ALL)

for names in cities:
    print(Fore.MAGENTA + f"({cities[names]['id']}) " + Style.RESET_ALL + names)

# City search engine
CITY=input("\nWybierz miasto\n> ")

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
except KeyError:
    print(Fore.RED + "Wybierz poprawne miasto!" + Style.RESET_ALL)
    sys.exit()

print(f"\n--- Pogoda w {CITY} ---") 

if temp > 0:
    print(Fore.YELLOW + f"- Temperatura: {temp} C" + Style.RESET_ALL)
elif temp <= 0:
    print("> Temperatura:", Fore.CYAN + f"{temp: .0f} C" + Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX + f"- Wilgotność powietrza: {humidity}%" + Style.RESET_ALL)
print(Fore.WHITE + f"- Zachmurzenie: {clouds}%\n" + Style.RESET_ALL)
sys.exit()

# Preparing more features
print(Fore.MAGENTA + "(1)" + Style.RESET_ALL, "Wyjście")

action_2 = input("Wybierz następne działanie\n> ")

if action_2 == '1':
    sys.exit()
else:
    print("Wybierz poprawną opcję!")
    sys.exit()