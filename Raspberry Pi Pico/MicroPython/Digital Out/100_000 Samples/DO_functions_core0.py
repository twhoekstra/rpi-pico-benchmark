import utime

LED_PIN = const(25) # 25 Raspberry Pi Pico
NUM_PULSES = const(100_000)

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f} ms'.format(myname, delta/1000))
        return result
    return new_func

def bytecode_out():
        
    from machine import Pin
    led = Pin(LED_PIN, Pin.OUT)

    for __ in range(NUM_PULSES):
        led.value(True)
        led.value(False)

@micropython.native
def native_out():
    from machine import Pin
    led = Pin(LED_PIN, Pin.OUT)

    for __ in range(NUM_PULSES):
        led.value(True)
        led.value(False)
   
@micropython.viper
def viper_out():
    from machine import Pin
    led = Pin(LED_PIN, Pin.OUT)

    for __ in range(NUM_PULSES):
        led.value(True)
        led.value(False)     








