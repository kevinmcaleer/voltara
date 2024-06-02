# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BCM) # Sets the pin numbering system to use the physical layout

# Set up pin 17 for PWM

class Head():

    def __init__(self):
        SERVO_PIN = 17
        GPIO.setup(SERVO_PIN,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
        self.p = GPIO.PWM(SERVO_PIN, 50)     # Sets up pin 11 as a PWM pin
        self.p.start(0)               # Starts running PWM on the pin and sets it to 0

        self.MOUTH_OPEN = 3
        self.MOUTH_CLOSED = 12
        # Move the servo back and forth

        self.DELAY = 0.02

    def open_close(self):
        # print("Opening mouth")
        for cycle in range(self.MOUTH_CLOSED*10, self.MOUTH_OPEN*10, -1):

            value = cycle/10
            self.p.ChangeDutyCycle(value)     # Changes the pulse width to 3 (so moves the servo)
            # print(f"Duty cycle is: {value}")
            sleep(self.DELAY)                 # Wait 1 second

        # print("Closing mouth")
        for cycle in range(self.MOUTH_OPEN*10, self.MOUTH_CLOSED*10):

            value = cycle/10
            self.p.ChangeDutyCycle(value)     # Changes the pulse width to 3 (so moves the servo)
            # print(f"Duty cycle is: {value}")
            sleep(self.DELAY)  

    def open(self):
         for cycle in range(self.MOUTH_CLOSED*10, self.MOUTH_OPEN*10, -1):

            value = cycle/10
            self.p.ChangeDutyCycle(value)     # Changes the pulse width to 3 (so moves the servo)
            # print(f"Duty cycle is: {value}")
            sleep(self.DELAY)    

    def close(self):
        for cycle in range(self.MOUTH_OPEN*10, self.MOUTH_CLOSED*10):

            value = cycle/10
            self.p.ChangeDutyCycle(value)     # Changes the pulse width to 3 (so moves the servo)
            # print(f"Duty cycle is: {value}")
            sleep(self.DELAY)  

    def stop(self):

        # Clean up everything
        self.p.stop()                 # At the end of the program, stop the PWM
        # GPIO.cleanup()           # Resets the GPIO pins back to defaults
