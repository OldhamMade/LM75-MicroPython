from machine import Pin, I2C
from math import floor
from time import sleep

D1 = Pin(5)  # SCL, GPIO5
D2 = Pin(4)  # SDA, GPIO4


class LM75(object):
    ADDRESS = 0x48
    FREQUENCY = 100000

    def __init__(self):
        self.i2c = I2C(scl=D1, sda=D2, freq=self.FREQUENCY)

    def get_output(self):
        """Return raw output from the LM75 sensor."""
        output = self.i2c.readfrom(self.ADDRESS, 2)
        return output[0], output[1]

    def get_temp(self):
        """Return a tuple of (temp_c, point)."""
        temp = self.get_output()
        return int(temp[0]), int(temp[1])


def print_temp():
    sensor = LM75()
    while True:
        temperature, point = sensor.get_temp()
        print("%s.%s" % (temperature, floor(point / 23)))
        sleep(1)
