from DO_functions_core0 import *
import gc
import utime

@timed_function
def Bytecode():
    bytecode_out()
        
@timed_function
def Native():
    native_out()
        
@timed_function
def Viper():
    viper_out()

Bytecode()
gc.collect()
utime.sleep(1)
Native()
gc.collect()
utime.sleep(1)
Viper()
utime.sleep(1)