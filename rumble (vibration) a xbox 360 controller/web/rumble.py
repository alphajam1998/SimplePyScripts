#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: http://stackoverflow.com/questions/19749404/

import ctypes


# Define necessary structures
class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [
        ("wLeftMotorSpeed", ctypes.c_ushort),
        ("wRightMotorSpeed", ctypes.c_ushort)
    ]

# Load Xinput.dll
xinput = ctypes.windll.xinput1_1

# Set up function argument types and return type
XInputSetState = xinput.XInputSetState
XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
XInputSetState.restype = ctypes.c_uint


def set_vibration(left_motor, right_motor, controller=0):
    if type(left_motor) == float:
        left_motor_value = int(left_motor * 65535)
    else:
        left_motor_value = left_motor

    if type(right_motor) == float:
        right_motor_value = int(right_motor * 65535)
    else:
        right_motor_value = right_motor

    vibration = XINPUT_VIBRATION(left_motor_value, right_motor_value)
    XInputSetState(controller, ctypes.byref(vibration))
