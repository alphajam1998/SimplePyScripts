#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install pyxDamerauLevenshtein
# https://github.com/gfairchild/pyxDamerauLevenshtein
# SOURCE: https://github.com/gfairchild/pyxDamerauLevenshtein/blob/master/examples/examples.py


ALL_COMMANDS = [
    'команды',
    'ругнись',
    'насмеши',
    'погода',
    'котики',
    'что посмотреть',
    'угадай',
    'hex2str', 'str2hex',
    'bin2str', 'str2bin',
    'qrcode',
    'добавь напоминание', 'удали напоминание',
    'короткая ссылка',
    'найди гифку',
    'курс валют',
    'курс криптовалют',
    'язык Йоды',
    'язык падонков', 'олбанский', 'олбанский язык',
    'православный язык',
]


def find_command(text):
    import numpy as np
    array = np.array(ALL_COMMANDS)

    from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance_ndarray, damerau_levenshtein_distance_ndarray
    result = list(zip(ALL_COMMANDS, list(normalized_damerau_levenshtein_distance_ndarray(text, array))))
    # print()
    # print(result)

    command, rate = min(result, key=lambda x: x[1])

    # Подобранное значение для определения совпадения текста среди указанного списка
    if rate > 0.25:
        return

    return command


if __name__ == '__main__':
    # SHOW RESULT
    def check(text):
        format_text = '{:<%s} -> {}' % (len(max(ALL_COMMANDS, key=len)) + 5)

        command = find_command(text)
        if command is None:
            result = 'is None (не удалось распознать команду: "{}")'.format(text)
            print(format_text.format(text, result))
        else:
            print(format_text.format(text, command))

    check('команды')
    check('комнды')
    check('команду')
    check('команду')
    check('комманды')
    check('короткую ссылку')
    check('курс валют')
    check('курсы валюты')
    check('добавь напоминание')
    check('добавь напаменание')
    check('добавить напоминание')
    check('добавить команду')

    #
    # Run test
    def run_tests():
        def test(text, expected):
            command = find_command(text)
            assert expected == command, 'Expected: "{}", get: "{}"'.format(expected, command)

        expected = 'команды'
        test('команды', expected)
        test('комнды', expected)
        test('команду', expected)
        test('команду', expected)
        test('комманды', expected)

        expected = 'короткая ссылка'
        test('короткую ссылку', expected)

        expected = 'курс валют'
        test('курс валют', expected)
        test('курсы валюты', expected)

        expected = 'добавь напоминание'
        test('добавь напоминание', expected)
        test('добавь напаменание', expected)
        test('добавить напоминание', expected)

        expected = None
        test('добавить команду', expected)
        test('купить слона', expected)
        test('кмнд', expected)

    run_tests()
