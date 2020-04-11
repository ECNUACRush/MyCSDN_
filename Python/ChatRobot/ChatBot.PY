import time
import random
import requests
from termcolor import colored
from simpleeval import simple_eval


class Bot:
    wait = 1

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'blue')

    def run(self):
        time.sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a != '':
                break
            print(self._format('Input valid, Please enter again!'))
        time.sleep(Bot.wait)
        print(self._format(self._think(self.a)))


class HelloBot(Bot):
    def __init__(self):
        self.q = 'Hi, What\'s your name?'

    def _think(self, s):
        return f'Hello, {s}!'


class GreetingBot(Bot):
    def __init__(self):
        self.q = 'Hi, what\'s your feeling now?'

    def _isgood(self, s):
        Pos = ['good', 'fine', 'ok', 'nice']
        tag = False
        for pp in Pos:
            if pp in s.lower():
                tag = True
        if 'not' in s.lower():
            tag = bool(1 - tag)
        return tag

    def _think(self, s):
        if self._isgood(s):
            return f'I feel fine, too!'
        else:
            return f'Sorry to hear that, Be cheerful! my friend.'


class FavColor(Bot):
    def __init__(self):
        self.q = 'Hi, what\'s your favorite color?'

    def _think(self, s):
        colors = ['white', 'purple', 'gray', 'pink']
        return f'Your favorite color is {s.lower()}, While my favorite is {random.choice(colors)}'


class WeatherBot(Bot):
    def __init__(self):
        self.q = 'Hello, I can do weather report for you! Please input city\'s name'

    def _think(self, s):
        city = self.a
        rep = requests.get(f'http://www.tianqiapi.com/api?version=v6&appid=23035354&appsecret=8YvlPNrz&city={city}')
        rep.encoding = 'utf-8'
        print('城市：%s' % rep.json()['city'])
        print('天气：%s' % rep.json()['wea'])
        print('风向：%s' % rep.json()['win'])
        print('温度：%s' % rep.json()['tem'] + '°C')
        print('风力：%s' % rep.json()['win_speed'])
        print('湿度：%s' % rep.json()['humidity'])
        print('空气质量：%s' % rep.json()['air_level'])
        return f'{city} forecast over'


class CalcBot(Bot):
    def __init__(self):
        self.q = 'Hello, my friend, I can do some scientific calculation for you'

    def calctime(self, num):
        # 假设此人每秒进行1e20次运算
        times = 1e20
        return num / times

    def run(self):
        Quit = ['x', 'q', 'exit', 'quit']
        while True:
            time.sleep(Bot.wait)
            print(self._format(self.q))
            self.a = input()
            if self.a.lower() in Quit:
                break
            try:
                result = simple_eval(self.a)
            except ZeroDivisionError as err:  # useful
                print(f'Oops!There are something unexpected happened:{err}, please enter again')
            else:
                self.wait = self.calctime(result)
                time.sleep(self.wait)
                print(self._format(f'Done! Result is {result}'))
        print(self._format('Calculation Over, Thanks for using'))


class AmazingPy(Bot):
    # 为了继承Bot中的_format方法不用重写
    def __init__(self, wait):
        Bot.wait = wait
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)

    def _myprint(self, s):
        print(s)
        print()

    def run(self):
        self._myprint(self._format('Hi, I\'m AI assistant made by Hz. Let\'s talk!'))
        for bot in self.bots:
            bot.run()


HZ = AmazingPy(1)
HZ.add(HelloBot())
HZ.add(GreetingBot())
HZ.add(FavColor())
HZ.add(CalcBot())
HZ.add(WeatherBot())
HZ.run()
