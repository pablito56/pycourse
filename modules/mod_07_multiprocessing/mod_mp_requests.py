#-*- coding: utf-8 -*-
u"""
MOD: Multiprocessing with requests
"""

import multiprocessing
import requests
from pprint import pprint
import threading


def get_weather(num):
    location = "41.41,2.22"
    key = "5nrhptjvus6gdnf9e6x75as9"
    num_days = 3
    url_pattern = "http://api.worldweatheronline.com/free/v1/weather.ashx?q={loc}&format=json&num_of_days={days}&key={key}"
    r = requests.get(url=url_pattern.format(loc=location, days=num_days, key=key),
                     headers={'content-type': 'application/json'})
    print "GET WEATHER", num
    pprint(r.json()["data"]["current_condition"][0])


def get_weather_3x_mp():
    p = multiprocessing.Pool(3)
    p.map(get_weather, range(3))


def get_weather_3x_th():
    threads = []
    for i in range(3):
        t = threading.Thread(target=get_weather, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    import time
    start_th = time.time()
    get_weather_3x_th()
    end_th = time.time()
    time.sleep(1)
    start_mp = time.time()
    p = multiprocessing.Pool(3)
    p.map(get_weather, range(3))
    end_mp = time.time()
    print "ELAPSED THREADING: {:.5f} seconds".format(end_th - start_th)
    print "ELAPSED MULTIPROCESSING: {:.5f} seconds".format(end_mp - start_mp)
