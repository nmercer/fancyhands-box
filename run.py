import RPi.GPIO as GPIO
import time

BUTTON_PIN = 25
LIGHT_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

prev_input = 1
while True:
  input = GPIO.input(BUTTON_PIN)

  if prev_input != input and not input:
    print("Button Pushed DOWN")
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
  elif prev_input != input and input:
    print("Button Released")
    GPIO.output(LIGHT_PIN, GPIO.LOW)
  prev_input = input
  time.sleep(0.05)
