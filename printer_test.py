#!/usr/bin/python

from Adafruit_Thermal import *
import gfx.adalogo as pixel_data

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.setTimes(35000, 2100)

printer.printBitmap(pixel_data.width, pixel_data.height, pixel_data.data)

printer.feed(2)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults