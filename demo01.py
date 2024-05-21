from voltara.message import Message
from Adafruit_Thermal import *
from time import sleep
from voltara.button import button

message = Message()

while KeyboardInterrupt:
    print("Press button for Fortune")
    button.wait_for_press()

    message.print_header()
    message.print_fortune()
    message.print_footer()
    sleep(5)

print("Done.")