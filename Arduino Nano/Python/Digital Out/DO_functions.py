# -*- coding: utf-8 -*-
"""

@author: twh
"""

import time

LED_PIN = 13 # 13 For Arduino Nano
NUM_PULSES = 100_000

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.time_ns()
        result = f(*args, **kwargs)
        delta = time.time_ns() - t
        print('Function {} Time = {:6.3f} ms'.format(myname, delta/1E6))
        return result
    return new_func

def timed_function_long(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.time()
        result = f(*args, **kwargs)
        delta = time.time() - t
        print('Function {} Time = {:6.3f} ms'.format(myname, delta*1000))
        return result
    return new_func

def digital_out(arduino):
    
    led = arduino.get_pin('d:'+str(LED_PIN)+':o')

    for __ in range(NUM_PULSES):
        led.write(True)
        led.write(False)