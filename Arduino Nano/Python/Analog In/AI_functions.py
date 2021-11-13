# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:14:50 2021

@author: twh
"""
import time
NUM_SAMPLES = 10000


def timed_function_long(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.time()
        result = f(*args, **kwargs)
        delta = time.time() - t
        print('Function {} Time = {:6.3f} ms'.format(myname, delta*1000))
        return result
    return new_func

def analog_read(arduino):
    a0 = arduino.get_pin('a:0:i')
    samples = [0 for __ in range(NUM_SAMPLES)]
    
    for ii in range(NUM_SAMPLES):
        samples[ii] = a0.read()
        time.sleep(1E-6) # Delay necessary to read properly
    