from DO_functions_core0 import *

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
Native()
Viper()