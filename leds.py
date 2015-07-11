#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys

DEBUG = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def init():

    print "Args: " + len(sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[0] == 1:
            print "GREEN"
            GPIO.output(GREEN_LED, True)
            GPIO.output(RED_LED, False)
        else:
            print "RED"
            GPIO.output(GREEN_LED, False)
            GPIO.output(RED_LED, True)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        init()
    finally:
        GPIO.cleanup()
