from AI_functions_core0 import *

@timed_function
def Bytecode():
    bytecode_read()
    
@timed_function
def Native():
    native_read()
    
@timed_function
def Viper():
    viper_read()

Bytecode()
Native()
Viper()
