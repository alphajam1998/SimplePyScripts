#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from multiprocessing import Process


def go(name):
    import tkinter as tk
    app = tk.Tk()
    app.minsize(150, 50)

    mw = tk.Label(app, text='Hello, ' + name)
    mw.pack(fill='both', expand=True)

    app.mainloop()


if __name__ == '__main__':
    p = Process(target=go, args=('bob',))
    p.start()
    p.join()
