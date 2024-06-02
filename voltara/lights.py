# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

class CystalBall():
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM) # Sets the pin numbering system to use the physical layout

        # Set up pin 17 for LED

        self.CRYSTAL_BALL_PIN = 21
        GPIO.setup(self.CRYSTAL_BALL_PIN,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)

    def on(self):
        # p.start(0)               # Starts running PWM on the pin and sets it to 0
        GPIO.output(self.CRYSTAL_BALL_PIN, GPIO.HIGH)
        
    def off(self):
        
        GPIO.output(self. CRYSTAL_BALL_PIN, GPIO.LOW)

    def stop(self):
        # Clean up everything
        # p.stop()                 # At the end of the program, stop the PWM
        GPIO.cleanup()           # Resets the GPIO pins back to defaults
