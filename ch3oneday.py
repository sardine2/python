# -*- coding: utf-8 -*-

import requests
import json
#import time
import datetime
import pypinyin as py


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
        clouds = '云量:' + str(data['clouds']['all']) + '%'
        wind = '风速:' + str(data['wind']['speed']) + 'meter/sec'
        #rain = '降雨指数'+ str(data['rain']['3h'])
        #onlinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        result = city, weather, description,temp,clouds,wind
        print(result)# here
        set_history01(city,weather,description,temp,clouds,wind)
    return city,weather,description,temp,clouds,wind


def set_history01(city,weather,description,temp,clouds,wind):
    number = len(history01)
    daytime = datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S')
    history01.append((number,daytime,city,weather,
                      description,temp,clouds,wind))


def fetch_history01():
    if len(history01)== 0:
        print('No history ~~')
    else:
        for history in set(history01):
            print(history)
            #print(history[0],history[1],history[2],history[3],history[4],
            #history[5],history[6],history[7],history[8])
    #return history01 #check here


def weather_search(m):
    while True:
        m = input('You can enter city name in Chinese or English:')
        if m == 'help':
            welcome()
        elif m == "history":
            fetch_history01()
        elif m == "quit":
            print('Goodbye!')
            quit()
        else:
            fetchAPI(m)


if __name__ == '__main__':

   history01 = []
   m = input
   weather_search(m)
