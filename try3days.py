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
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
    payload = {'APPID':'90cb9d98ac5f5c13cc6c2ab80ab5a024','q':city,
    'units':'metric','cnt':3,'lang':'zh_cn'}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)
    return data

    #if r.status_code != requests.codes.ok:
    #    return 'sorry,please try again.'
    #else:

def three_days(data,city):
    day = []
    result = []

    for i in range(0,3):
        day.append(data['list'][i])

    for i in range(0,3):
        result.append(str(datetime.datetime.fromtimestamp(data['list'][i]['dt']).strftime('%Y-%m-%d %H:%M:%S')),
        data['list'][i]['weather'][0]['main'],data['list'][i]['weather'][0]['description'],
        str(data['list'][i]['temp']['day'])+'℃','气压:' + str(data['list'][i]['pressure']) + 'hPa',
        '湿度:' + str(data['list'][i]['humidity']) + '%')
    return result

'''
    for dayt,weather,description,temp,pressure,humidity in result:
        result[dayt] = str(datetime.datetime.fromtimestamp(data['list'][m]['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        result[weather] = data['list'][m]['weather'][0]['main']  # to fetch the 'weather' data from a dict in a list,sounds terrible.
        result[description] = data['list'][m]['weather'][0]['description']
        result[temp] = str(data['list'][m]['temp']['day'])+'℃'
        result[pressure] = '气压:' + str(data['list'][m]['pressure']) + 'hPa'
        result[humidity] = '湿度:' + str(data['list'][m]['humidity']) + '%'

        print(result.values())# here
        dayt = str(datetime.datetime.fromtimestamp(day[m]['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        weather = day[m]['weather'][0]['main']  # to fetch the 'weather' data from a dict in a list,sounds terrible.
        description = day[m]['weather'][0]['description']
        temp = str(day[m]['temp']['day'])+'℃'
        pressure = '气压:' + str(day[m]['pressure']) + 'hPa'
        humidity = '湿度:' + str(day[m]'humidity']) + '%'
'''
#        set_history01(city,dayt,weather,description,temp,pressure,humidity)



def set_history01(city,dayt,weather,description,temp,pressure,humidity):
    number = len(history01)
    daytime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history01.append((number,daytime,city,dayt,weather,description,
                    temp,pressure,humidity))

def fetch_history01():
    if len(history01)== 0:
        print('No history ~~')
    else:
        for history in set(history01):
            print(history)



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
            data = fetchAPI(m)
            if 'status' in data:
                print('no resule ~ ~')
            else:
                result = three_days(data,m)  # here m is important
                i = input('Type please the number 0,1,2 see what may happen:')
                while True:
                    #i = int(m) - 1
                    if i in [0,1,2]:


                        print(result[i])

                    else:
                        m = input('Try again? please the number 0,1,2 see what may happen?')

if __name__ == '__main__':

   history01 = []
   m = input
   weather_search(m)
