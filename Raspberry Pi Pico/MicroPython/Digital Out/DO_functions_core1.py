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

def bytecode_out(baton):
    baton.acquire()
    from machine import Pin
    led = Pin(25, Pin.OUT)

    for __ in range(1_000_000):
        led.value(True)
        led.value(False)
    baton.release()

@micropython.native
def native_out(baton):
    baton.acquire()
    from machine import Pin
    led = Pin(25, Pin.OUT)

    for __ in range(1_000_000):
        led.value(True)
        led.value(False)
    baton.release()
   
@micropython.viper
def viper_out(baton):
    baton.acquire()
    from machine import Pin
    led = Pin(25, Pin.OUT)

    for __ in range(1_000_000):
        led.value(True)
        led.value(False)
    baton.release()









