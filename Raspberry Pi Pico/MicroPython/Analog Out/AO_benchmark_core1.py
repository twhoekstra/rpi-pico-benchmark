NUM_PULSES = const(100_000)

import nb2211
import utime
import _thread

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f} ms'.format(myname, delta/1000))
        return result
    return new_func
    
### Create Write Command Registers ###
pico = nb2211.Pico()
byte_array = pico.__bake_spi_instructions([3, 0])


### Create Lock object for Thread Sync ###
baton = _thread.allocate_lock()

### Create function run in new thread ###
def analog_out(baton, pico, byte_array):
    baton.acquire()
    
    ### Pin Setup ###
    spi, CS, LDAC = pico.__setup_spi()
    CS.value(True)
    LDAC.value(False)

    ### Write Command Register Buffer Setup ###
    mv = memoryview(byte_array)
    resolution = len(byte_array)
    buffer = bytearray([0,0])

    for ii in range(0, NUM_PULSES*4, 2):
        # PREPARE ---------------------------    
        CS.value(False)
        buffer[0] = mv[ii%resolution]
        buffer[1] = mv[ii%resolution+1]

        # WRITE POINT -----------------------------
        spi.write(buffer)
        CS.value(True) # Datasheet: Chip select to end before LDAC pulse
    baton.release()
  
@timed_function
def analog_out_thread():
    _thread.start_new_thread(analog_out, (baton, pico, byte_array))
    utime.sleep_ms(10) # Delay before checking if function has ended
    baton.acquire() # Wait for function to end
    baton.release()
    
analog_out_thread()
print("\nDone!")
