import serial
from voltara.button import button
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.setTimes(35000, 2100)
# printer.feed(2)

# printer.testPage()

while  KeyboardInterrupt:
    button.wait_for_press()

    printer.feed(5)

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

    printer.feed(4)
    printer.reset()