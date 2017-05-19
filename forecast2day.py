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


    if r.status_code != requests.codes.ok:
        return 'sorry,please try again.'
    else:


        timestamp0 = data['list'][0]['dt']
        dayt0 = str(datetime.datetime.fromtimestamp(timestamp0).strftime('%Y-%m-%d %H:%M:%S'))
        weather0 = data['list'][0]['weather'][0]['main']  # to fetch the 'weather' data from a dict in a list,sounds terrible.
        description0 = data['list'][0]['weather'][0]['description']
        temp0 = str(data['list'][0]['main']['temp'])+'℃'
        clouds0 = '云量:' + str(data['list'][0]['clouds']['all']) + '%'
        wind0 = '风速:' + str(data['list'][0]['wind']['speed']) + 'meter/sec'
        #rain = '降雨指数'+ str(data['rain']['3h'])
        #onlinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        time_txt0 = '这大概是数据运算时间：'+ str(data['list'][0]['dt_txt'])

        timestamp1 = data['list'][1]['dt']
        dayt1 = str(datetime.datetime.fromtimestamp(timestamp1).strftime('%Y-%m-%d %H:%M:%S'))
        weather1 = data['list'][1]['weather'][0]['main']  # to fetch the 'weather' data from a dict in a list,sounds terrible.
        description1 = data['list'][1]['weather'][0]['description']
        temp1 = str(data['list'][1]['main']['temp'])+'℃'
        clouds1 = '云量:' + str(data['list'][1]['clouds']['all']) + '%'
        wind1 = '风速:' + str(data['list'][1]['wind']['speed']) + 'meter/sec'
        #rain = '降雨指数'+ str(data['rain']['3h'])
        #onlinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        time_txt1 = '这大概是数据运算时间：'+ str(data['list'][1]['dt_txt'])



        result0 = city,dayt0,weather0,description0,temp0,clouds0,wind0,time_txt0
        result1 = city,dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1

        print(result0,result1)# here
        set_history01(city,dayt0,weather0,description0,temp0,clouds0,wind0,time_txt0,
                      dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1)
    #return city,dayt0,weather0,description0,temp0,clouds0,wind0,time_txt0,
    #       dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1



def set_history01(city,dayt0,weather0,description0,temp0,clouds0,wind0,time_txt0,
              dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1):
    number = len(history01)
    daytime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history01.append((number,daytime,city,dayt0,weather0,description0,temp0,clouds0,wind0,time_txt0,
                  dayt1,weather1,description1,temp1,clouds1,wind1,time_txt1))


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
