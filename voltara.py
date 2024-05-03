import serial
from gpiozero import Button
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.setTimes(35000, 2100)
printer.feed(2)

button = Button(23)

button.wait_for_press()

printer.feed(2)

printer.underlineOn()
printer.setSize("M")
printer.justify('C')
printer.print(' --= Voltara Fortune Teller =--\n\n')
printer.underlineOff()
printer.setSize("S")
printer.justify("L")
printer.feed(2)
printer.print("Your Wish is granted")
printer.feed(2)
printer.print("----------------------------------")
printer.print("https://www.kevsrobots.com/voltara")
