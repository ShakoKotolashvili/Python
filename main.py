# import requests
# import json
#
# api_key = "af8fffd40d731fc1a44ffa12ca61beea"
# city_name = input("შეიყვანეთ ქალაქის სახელი: ")
# url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
#
# r = requests.get(url)
#
# print(r)
# print(r.headers)
# print(r.text)
# print(r.status_code)
#
#
# weather_data = r.json()
# if weather_data['cod'] == 200:
#
#     kelvin = 273.15
#     temp = int(weather_data['main']['temp'] - kelvin)
#     cloudy = weather_data['clouds']['all']
#     humidity = weather_data['main']['humidity']
#     pressure = weather_data['main']['pressure']
#     wind_speed = weather_data['wind']['speed'] * 3.6
#     description = weather_data['weather'][0]['description']
#
#     print(f'ამინდი ქალაქში: {city_name}')
#     print(f'ტემპერატურა: {temp} ცელსიუს გრადუსი')
#     print(f'ღრუბლიანობა: {cloudy}%')
#     print(f'ტენიანობა: {humidity}%')
#     print(f'წნევა: {pressure} პასკალი')
#     print(f'ქარის სიჩქარე: {wind_speed} კმ/სთ')
#     print(f'ძირითადი ამინდის ინფორმაცია: {description}')
#
# else:
#
#     print(f'ქალაქი {city_name} ვერ მოიძებნა')



import requests
import json

api_key = "af8fffd40d731fc1a44ffa12ca61beea"
city_name = "Berlin"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
print(url)

r = requests.get(url)
print(r)
print(r.headers)
print(r.text)
print(r.status_code)

data = r.json()

#აქ ვპოულობ ქალაქის სახელს, მის გრძედსა და განედს.

name = data['name']
lon = data['coord']['lon']
lat = data['coord']['lat']

print(f'ქალაქ {name} - ის გრძედი და განედია: {lon}, {lat}')

exclude = "minute,hourly"
url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}'
print(url2)

req2 = requests.get(url2)
data2 = req2.json()

#ტემპერატურა დღისა და ღამის განმავლობაში
days = []
nights = []
description = []

for i in data2['daily']:

    days.append(round(i['temp']['day'] - 273.15, 2))
    nights.append(round(i['temp']['night'] - 273.15, 2))

    description.append(i['weather'][0]['main'] + ": " + i['weather'][0]['description'])

#დამრგვალებული ტემპერატურა დღისა და ღამის განმავლობაში

print(days)
print(nights)
print(description)

string = f'{name} - 8 დღის ამინდის პროგნოზი\n'

for i in range(len(days)):
    if i == 0:
        string += f'\nდღე {i+1} (დღეს)\n'

    elif i == 1:
        string += f'\nდღე {i+1} (ხვალ)\n'

    else:
        string += f'\nდღე {i+1}\n'

    string += 'დილა: ' + str(days[i]) + ' ცელსიუს გრადუსი' + "\n"
    string += 'ღამე: ' + str(nights[i]) + ' ცელსიუს გრადუსი' + "\n"
    string += 'ზოგადი ამინდი: ' +description[i] + "\n"

print(string)