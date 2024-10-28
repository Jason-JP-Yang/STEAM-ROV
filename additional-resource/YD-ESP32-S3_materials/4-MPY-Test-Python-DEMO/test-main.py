from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(16, Pin.OUT)   
np = NeoPixel(pin, 1)   
np[0] = (10,0,0) 
np.write()              
