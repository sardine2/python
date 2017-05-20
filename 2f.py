# -*- coding: utf-8 -*-

import requests
import json
#import time
import datetime
#import pypinyin as py


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
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    payload = {'APPID':'90cb9d98ac5f5c13cc6c2ab80ab5a024','q':city,
    'units':'metric','lang':'zh_cn'}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)
    return data


#if r.status_code != requests.codes.ok:
#    return 'sorry,please try again.'
#else:

def three_days(data):
    day0 = data['list'][0]
    day1 = data['list'][4]
    day2 = data['list'][20]
    return day0,day1,day3


def daily_data(list,city):
    timestamp = list['dt']
    dayt = str(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
    weather = list['main']
    description = list['description']
    temp0 = str(list['temp'])+'℃'
    clouds0 = '云量:' + str(list['all']) + '%'
    wind0 = '风速:' + str(list['speed']) + 'meter/sec'
    time_txt = '这大概是数据运算时间：'+ str(list['dt_txt'])
    result = city,dayt,weather,description,temp,clouds,wind,time_txt
    #result1 = city,dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1

    #    print(result0,result1)# here
    set_history01(result)
    return city,dayt,weather,description,temp,clouds,wind,time_txt
    #       dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1



def set_history01(result0):
    number = len(history01)
    daytime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history01.append((number,daytime,result))


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

            data = fetchAPI(m)
            if 'status' in data:
                print('Dear,what is happending?')

            else:
                a,b,c = three_days(data)
                m = input('Type the day '1,2,3' you want to search:')
                while True:
                    if m == '1':
                        show = get_data(a,day0)
                        print(show)
                        history01.append((number,daytime,city,dayt,weather,
                      description,temp,clouds,wind,time_txt))
                        #break
                    elif m == '2':
                        show = get_data(b,m)
                        print(show)
                        history01.append((number,daytime,city,dayt,weather,
                        description,temp,clouds,wind,time_txt))
    #                    break
                    elif m == '3':
                        show = get_data(c,m)
                        print(show)
                        history01.append((number,daytime,city,dayt,weather,
                              description,temp,clouds,wind,time_txt))
        #                break
                        else:
                            m = input('try again ?')


if __name__ == '__main__':

   history01 = []
   m = input
   weather_search(m)
