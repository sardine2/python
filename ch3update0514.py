# -*- coding: utf-8 -*-

import requests
import json
import time


def welcome():
    print('''
    Hello! Here are the Local Weather Forecast.
    Type the city name you want to search in Chinese or English.
    Type  "help" to get more help.
    Type "history" to get the search history records.
    Type "quit" to quit the program.
    Clouds of city in China is not subscriptable, you know why.
    ''')
welcome()

def fetchAPI(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'APPID':'90cb9d98ac5f5c13cc6c2ab80ab5a024','q':city,
    'units':'metric','lang':'zh_cn'}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)

    if r.status_code != requests.codes.ok:
        return 'sorry,please try again.'
    else:
        weather = data['weather'][0]['main'] # to fetch the 'weather' data from a dict in a list,sounds terrible.
        description = data['weather'][0]['description']
        temp = str(data['main']['temp'])+'℃'
        clouds = '云量' + str(data['clouds']['all'])
        wind = str(data['wind']['speed']) + 'meter/sec'
        #rain = '降雨指数'+ str(data['rain']['3h'])
        onlinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        result = onlinetime,city, weather, description,temp,clouds,wind
        print(result)# here
    return onlinetime, weather,description,temp,clouds,wind



searchHistory = []

while True:
    m = input('You can enter city name in Chinese or English:')
    if m == 'help':
        print('''
        Enter city name to get the weather conditions,
        Enter help,to get more help,
        Enter history,to get the searchHistory,
        Enter quit or exit to quit.
        ''')
    elif m == "history":
        if len(searchHistory) == 0:
            print("No history records.")
        else:
            for i in searchHistory:
                print(searchHistory)

    elif m == "quit":
       print('Goodbye!')
       quit()
    else:
        fetchAPI(m)
        searchHistory.append(m) #put searchHistory.append(m) to get history
