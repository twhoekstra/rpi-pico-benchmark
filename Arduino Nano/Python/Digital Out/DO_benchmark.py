# -*- coding: utf-8 -*-
"""

@author: twh
"""
import pyfirmata
import time
import gc
from DO_functions import timed_function, timed_function_long, digital_out

arduino = pyfirmata.ArduinoNano('COM9') #ADAPT THE COM PORT TO YOUR SYSTEM
time.sleep(1)

it = pyfirmata.util.Iterator(arduino)
it.start()

@timed_function_long
def Digital():
    digital_out(arduino)
        
Digital()

gc.collect()
time.sleep(1)

arduino.sp.close()