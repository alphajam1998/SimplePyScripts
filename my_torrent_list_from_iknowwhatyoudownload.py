#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""
Скрипт, используя сервис http://iknowwhatyoudownload.com показывает список торрентов текущего ip,
попавшего в базу сервиса.

"""


import requests
from bs4 import BeautifulSoup
import time


while True:
    try:
        rs = requests.get('http://iknowwhatyoudownload.com/ru/peer/', headers={'User-Agent': '-'})
        root = BeautifulSoup(rs.content, 'lxml')

        items = [item.text.strip() for item in root.select('.torrent_files > a')]
        print(len(items), items)

        # Every 12 hours
        time.sleep(60 * 60 * 12)

    except Exception as e:
        print('Error:', e)
