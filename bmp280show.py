from machine import I2C
from bmp280 import BMP280
 
bus = I2C(sda=Pin(21),scl=Pin(22))
bmp = BMP280(bus)
 
print(bmp.temperature)
print(bmp.pressure)