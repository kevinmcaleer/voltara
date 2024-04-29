import Adafruit_Thermal as adafruit_thermal_printer
from fortune import fortune
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)



ThmeralPrinter = adafruit_thermal_printer.get_printer_class(2.68)

printer = ThmeralPrinter(uart)

printer.test_page()
printer.feed(2)

printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
printer.size = adafruit_thermal_printer.SIZE_MEDIUM
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.print(' --= Voltara Fortune Teller =--\n\n')
printer.underline = None
printer.sie = adafruit_thermal_printer.SIZE_SMALL
printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
printer.feed(2)
printer.print(fortune())
printer.feed(2)
printer.print("----------------------------------")
printer.print("https://www.kevsrobots.com/voltara")