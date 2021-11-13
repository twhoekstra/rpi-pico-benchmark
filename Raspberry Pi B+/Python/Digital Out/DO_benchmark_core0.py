from DO_functions_core0 import timed_function, digital_out
import gc
import time

@timed_function
def Digital_RPi_B():
    digital_out()
        
Digital_RPi_B()
gc.collect()
time.sleep(1)
