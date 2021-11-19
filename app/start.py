from machine import Pin
from time import sleep

print('Version 2 installed using USB')

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(0.5)
