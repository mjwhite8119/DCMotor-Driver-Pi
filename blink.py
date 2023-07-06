import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW) # Set pin 17 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(led_pin, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(led_pin, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second