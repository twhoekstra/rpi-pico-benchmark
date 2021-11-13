import time

LED_PIN = 23 # No LED Pin on Rasberry Pi B+
NUM_PULSES = 100_000

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.time_ns()
        result = f(*args, **kwargs)
        delta = time.time_ns() - t
        print('Function {} Time = {:6.3f} ms'.format(myname, delta/1E6))
        return result
    return new_func

def digital_out():
    import gpiozero

    led = gpiozero.DigitalOutputDevice(LED_PIN)

    for __ in range(NUM_PULSES):
        led.on()
        led.off()

