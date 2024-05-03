
from gpiozero import Button

button = Button(23)

button.wait_for_press()
print("button pressed")

