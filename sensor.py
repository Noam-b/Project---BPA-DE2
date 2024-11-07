import machine
import hcsr04
import time

ultrasonic = hcsr04.HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)

while True:
    distance = ultrasonic.distance_cm()
    if distance <= 10:
        #keep brightness of all seven segments high
    else:
        #reduce brightness of all seven segments
    time.sleep_ms(1000)
