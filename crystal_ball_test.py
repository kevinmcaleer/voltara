# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BCM) # Sets the pin numbering system to use the physical layout

# Set up pin 17 for LED

CRYSTAL_BALL_PIN = 21
GPIO.setup(CRYSTAL_BALL_PIN,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
GPIO.output(CRYSTAL_BALL_PIN, GPIO.LOW)
sleep(1)

# p.start(0)               # Starts running PWM on the pin and sets it to 0
GPIO.output(CRYSTAL_BALL_PIN, GPIO.HIGH)
sleep(5)
GPIO.output(CRYSTAL_BALL_PIN, GPIO.LOW)

# Clean up everything
# p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()           # Resets the GPIO pins back to defaults
