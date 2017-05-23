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
    'units':'metric','cnt':5,'lang':'zh_cn'}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)
    return data

    #if r.status_code != requests.codes.ok:
    #    return 'sorry,please try again.'
    #else:

def three_days(data,city):
    day = []
    result = []

    for i in range(0,5):
        day.append(data['list'][i])
        #print(day[i])

    #for i in range(0,2):
        #for dayt,weather,description,temp,pressure,humidity in result:
        dayt = str(datetime.datetime.fromtimestamp(day[i]['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        weather = day[i]['weather'][0]['main']  # to fetch the 'weather' data from a dict in a list,sounds terrible.
        description = day[i]['weather'][0]['description']
        temp = str(day[i]['temp']['day'])+'℃'
        pressure = '气压:' + str(day[i]['pressure']) + 'hPa'
        humidity = '湿度:' + str(day[i]['humidity']) + '%'
        result.append([city,dayt,weather,description,temp,pressure,humidity])
        #print(result)
    return result




def set_history01(result):
    number = len(history01)
    daytime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #for x in result:
    history01.append(number,daytime,result)
    #print(history01)

def fetch_history01():
    if len(history01)== 0:
        print('No history ~~')
    else:
        for y in history01:
            print(y)



def weather_search():
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

                i = input('Type please the number 1,2,3,4,5 \n for each 5 days forecast,and type 6 for all 5 days forecast:')
                result = three_days(data,m)  # here m is important
                while True:
                        try:
                            i = int(i) - 1
                            if i in [0,1,2,3,4]:
                                print(result[i])
                                history01.append(result[i])
                                break
                            if i == 5:
                                for x in result:
                                    print(x)
                                history01.append(x)

                            else:
                                i = input('Try again? please the number 0,1,2 see what may happen?')
                        except ValueError:
                                print('please only type the number between 1,2,3')

if __name__ == '__main__':

   history01 = []
   #m = input
   weather_search()
