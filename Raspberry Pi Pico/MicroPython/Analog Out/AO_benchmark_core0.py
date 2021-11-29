NUM_PULSES = const(100_000)

import nb2211
import utime

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f} ms'.format(myname, delta/1000))
        return result
    return new_func

pico = nb2211.Pico()

### Create Write Command Registers ###
byte_array = pico.__bake_spi_instructions([3, 0])

@timed_function
def analog_out(pico, byte_array):
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
  
    
analog_out(pico, byte_array)
print("\nDone!")
