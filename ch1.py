#coding:utf-8


d = {}
history01 = []

def weather_dict01():
    f = open('weather_info.txt','r').readlines()
    for line in f:
        data1 = line.split(',')
        d[data1[0]] = data1[1].strip()



def weather_search():
    while True:
        i = input('please enter the city name you want to search in chinese:')
        i = i.lower()
        if i in d:
            print(i + '天气为：'+ d[i])
            history01.append(i)
        elif i == 'history':
            for a in history01:
                print('What you need to know:'+ a,d[a])
        elif i == 'help':
            w_help()
        elif i == 'quit':
            quit()
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
   weather_dict01()
   weather_search()
