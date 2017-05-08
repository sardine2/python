#coding:utf-8

import datetime

def weather_dict01():
    d = {}
    f = open('weather_info.txt','r').readlines()
    for line in f:
        data1 = line.split(',')
        d[data1[0]] = data1[1].strip()
    return d

def set_history01(city,info):
    number = len(history01)
    daytime = datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S')
    history01.append(tuple((number,daytime,city,info)))
    '''f(a, b, c) is a function call with three arguments,
    while f((a, b, c))is a function call with a 3-tuple as the
    sole argument.'''

def fetch_history01():  #args??
    if len(history01)== 0:
        print('No history ~~')
    for history in history01:
        print(history[0],history[1],history[2],history[3])
    #return history01 #check here

def get_info(city,info):
    print('%s 的天气状况是 %s' % (city,info[city]))
    set_history01(city,info[city])
    #return d[i]

def quit_w():
    if len(history01)!= 0:
        fetch_history01()
    exit(0)

def input_city():
    i = input('please enter the city name you want to search in chinese:')
    return i


def weather_search(info):
    while True:
        city = input_city().strip().lower()
        if city == 'quit':
            print(len(history01))
            quit_w()
        elif city == 'history' or city == '历史':
            fetch_history01()
                #print('What you need to know:'+ a,d[a])
        elif city == 'help':
            w_help()
        elif city in info.keys():
            get_info(city,info)
        else:
            print('sorry,please try again later')

def w_help():
    print('''
        Type the city name you want to search and then press the
        enter/return botton,you will get the forecast.
        Type history you can get the search history,
        Type quit then you will quit this program.
        ''')


if __name__ == '__main__':

   history01 = []
   weather_dict01()
   d = weather_dict01()
   weather_search(d)
