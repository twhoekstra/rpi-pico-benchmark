import utime
import array

num_samples = const(10000)

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f} ms'.format(myname, delta/1000))
        return result
    return new_func

def bytecode_read():
    from machine import Pin, ADC
    a0 = ADC(Pin(32)) 

    samples = [0 for __ in range(num_samples)]

    for ii in range(num_samples):
        samples[ii] = a0.read_u16()

#@micropython.native
#def native_read(): ## Does not cross-compile
#    from machine import Pin, ADC
#    a0 = ADC(Pin(32))
#    
#    samples = [0 for __ in range(num_samples)]
#
#    for ii in range(num_samples):
#        samples[ii] = a0.read_u16()

#@micropython.viper     
#def viper_read(): ## Does not cross-compile
#    from machine import Pin, ADC
#    a0 = ADC(Pin(32))
#    
#    samples = [0 for __ in range(num_samples)]

    for ii in range(num_samples):
        samples[ii] = a0.read_u16()