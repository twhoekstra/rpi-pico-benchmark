# -*- coding: utf-8 -*-
"""

@author: twh
"""

import pyfirmata
import time
import gc
from AI_functions import timed_function_long, analog_read

arduino = pyfirmata.ArduinoNano('COM9') #ADAPT THE COM PORT TO YOUR SYSTEM

time.sleep(0.1)
it = pyfirmata.util.Iterator(arduino)
it.start()

@timed_function_long
def Analog_Nano():
    analog_read(arduino)
        
Analog_Nano()

gc.collect()
time.sleep(0.1)

arduino.sp.close()