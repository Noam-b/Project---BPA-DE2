
#this code change the luminosity of the clock depending if there is a presence or not.

import machine
import neopixel
import hcsr04
import time
import utime

ultrasonic = hcsr04.HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)
Pin = Pin(3, PIN.OUT) # Broche GPIO où sont connectées les LEDs
NumPixels = 14  # Nombre total de LEDs
np = neopixel.NeoPixel(Pin, NumPixels)

while True:
    distance = ultrasonic.distance_cm()
    if distance <= 10:
        #keep brightness of all seven segments high
        for i in range(NumPixels):
            np[i] = (255,0,0)
        np.write()
    else:
        #reduce brightness of all seven segments
         for i in range(NumPixels):
            np[i] = (100,0,0)
        np.write()
    time.sleep_ms(1000)
