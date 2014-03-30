#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import requests

from requests_oauthlib import OAuth1
from datetime import datetime
from settings import *

VOICE_POST_URL = 'http://10.0.1.20:8080/api/v1/attachments/upload/'
TEST_FILE = {'file': open('foo.txt', 'rb')}

BUTTON_PIN = 25
LIGHT_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

AUTH = OAuth1(FANCYHANDS_API_KEY, FANCYHANDS_API_SECRET)
#'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

def upload_file():
  r = requests.post(VOICE_POST_URL, TEST_FILE, auth=AUTH)
  print r.status_code
  
prev_input = 1

while True:
  input = GPIO.input(BUTTON_PIN)

  if prev_input != input and not input:
    start = datetime.now()
    print("Button Pushed DOWN")
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
  elif prev_input != input and input:
    time_pressed = (datetime.now()-start).total_seconds()
    GPIO.output(LIGHT_PIN, GPIO.LOW)
    print("Button Released")
    print('Seconds Pressed: %s' % time_pressed)
    upload_file()

  prev_input = input
  time.sleep(0.05)
