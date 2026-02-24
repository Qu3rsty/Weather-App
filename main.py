# libriaries
import requests
from colorama import Fore, Style
import sys
import json
import time

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
    wind_speed = data['wind']['speed'] 
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
time.sleep(5)

# Preparing more features
print(Fore.MAGENTA + "--- NASTEPNE OPCJE ---" + Style.RESET_ALL)
print(Fore.MAGENTA + "(1)" + Style.RESET_ALL, "Wyjście")
print(Fore.MAGENTA + "(2)" + Style.RESET_ALL, "Wyświetl alerty pogodowe")

action_2 = input("\nWybierz następne działanie\n> ")

if action_2 == '1':
    sys.exit()
elif action_2 == '2':
    print(Fore.MAGENTA + "--- ALERTY POGODOWE ---" + Style.RESET_ALL)
    if temp > 30:
        print(Fore.RED + "- Temperatura przekracza 30C!" + Style.RESET_ALL)
    elif temp < -5:
        print(Fore.CYAN + "- Temperatura jest niższa niż -5C!" + Style.RESET_ALL)
    else:
        pass
    if wind_speed > 70:
        print(Fore.RED + "- Prędkość wiatru przekracza 70km/h!" + Style.RESET_ALL)
    else:
        pass
    if not temp > 30 and not temp < -5 and not wind_speed > 70:
        print("Brak alertów pogodowych :D")
    elif temp > 30 or temp < -5 and wind_speed > 70:
        print("\nLepiej nie wychodź dzisiaj z domu")
else:
    print(Fore.RED + "Wybierz poprawną opcję!" + Style.RESET_ALL)
    sys.exit()