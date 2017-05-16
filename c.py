# -*- coding: utf-8 -*-

import requests
import json
import time


def welcome():
    print('''
    Hello!Here are the Local Weather Forecast.
    Enter the city you want to search in Chinese or English.
    Enter "help" to get more help.
    Enter "history" to get the search history records.
    Enter "quit" to quit the program.
    ''')
welcome()

def fetchAPI(city):
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    payload = {'APPID':'90cb9d98ac5f5c13cc6c2ab80ab5a024','q':city, 'lang':'zh_cn'}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)

    if r.status_code != requests.codes.ok:
        return 'sorry,please try again.'
    else:
        weather = data['weather'][0]['description'] # to fetch the 'weather' data from a dict in a list,sounds terrible.
        temp = str(data['main']['temp'])+'℉'
        wind = str(data['wind']['speed']) + 'miles/hour'
        onlinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        result = city, weather, temp, wind
        print(result)# here
        searchHistory.append(result)
    return onlinetime, weather, temp, wind



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
                print(i,searchHistory[i])
                searchHistory.append(i)
    elif m == "quit":
       print('Goodbye!')
       quit()
    else:
        fetchAPI(m)
