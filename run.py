#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from datetime import datetime

BUTTON_PIN = 25
LIGHT_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

prev_input = 1

while True:
  input = GPIO.input(BUTTON_PIN)

  if prev_input != input and not input:
    start = datetime.now()
    print("Button Pushed DOWN")
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
  elif prev_input != input and input:
    time_pressed = (start-datetime.now()).total_seconds()
    GPIO.output(LIGHT_PIN, GPIO.LOW)
    print("Button Released")
    print('Seconds Pressed: %s' % time_pressed)

  prev_input = input
  time.sleep(0.05)
