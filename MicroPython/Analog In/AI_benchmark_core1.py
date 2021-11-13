from AI_functions_core1 import *
import _thread

baton = _thread.allocate_lock()

@timed_function
def Bytecode():
    _thread.start_new_thread(bytecode_read, (baton,))
    utime.sleep_ms(10) # Delay before checking if function has ended
    baton.acquire() # Wait for function to end
    baton.release()

@timed_function
def Native():
    _thread.start_new_thread(native_read, (baton,))
    utime.sleep_ms(10)
    baton.acquire() # Wait for function
    baton.release()
    
@timed_function
def Viper():
    _thread.start_new_thread(viper_read, (baton,))
    utime.sleep_ms(10)
    baton.acquire() # Wait for function
    baton.release()
    
Bytecode()
Native()
Viper()





