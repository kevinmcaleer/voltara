import serial
from voltara.button import button
from voltara.lights import CystalBall
from voltara.head import Head
from Adafruit_Thermal import *
from time import sleep

ball = CystalBall()
head = Head()
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.setTimes(35000, 2100)
# printer.feed(2)

# printer.testPage()

while  KeyboardInterrupt:
    print("Press button for Fortune")
    button.wait_for_press()

    ball.on()
    head.open_close()

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
    sleep(5)
    ball.off()
    ball.stop()
    head.stop()