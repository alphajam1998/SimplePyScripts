#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'
 
 
"""Скрипт отправляет win7 в режим гибернации (спящий режим)"""
 
if __name__ == '__main__':
   import os
   os.system(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Hibernate')
