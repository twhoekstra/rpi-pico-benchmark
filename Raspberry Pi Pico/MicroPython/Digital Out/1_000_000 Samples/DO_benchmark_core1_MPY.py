from DO_functions_core1_MPY import *
import _thread

baton = _thread.allocate_lock()

@timed_function
def Bytecode_MPY():
    _thread.start_new_thread(bytecode_out, (baton,))
    utime.sleep_ms(10) # Delay before checking if function has ended
    baton.acquire() # Wait for function to end
    baton.release()
    
Bytecode_MPY()






