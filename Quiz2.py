import RPi.GPIO as GPIO
import time

# Pin setup
redPin = 5
greenPin = 6
bluePin = 13

buttonRed = 18
buttonGreen = 23
buttonBlue = 24

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set up LED pins as outputs
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

# Set up button pins as inputs with pull-up resistors
GPIO.setup(buttonRed, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonGreen, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonBlue, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to update LED states
def update_leds():
    redState = GPIO.input(buttonRed)
    greenState = GPIO.input(buttonGreen)
    blueState = GPIO.input(buttonBlue)

    GPIO.output(redPin, not redState)
    GPIO.output(greenPin, not greenState)
    GPIO.output(bluePin, not blueState)

try:
    while True:
        update_leds()
        time.sleep(0.01)  # Small delay to debounce
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

