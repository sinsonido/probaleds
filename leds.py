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

    print "Args: " + str(len(sys.argv)) + " - " + str(sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[1] == "GREEN":
            print "GREEN"
            GPIO.output(GREEN_LED, True)
            GPIO.output(RED_LED, False)
        elif sys.argv[1] == "RED":
            print "RED"
            GPIO.output(GREEN_LED, False)
            GPIO.output(RED_LED, True)

    GPIO.cleanup()

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        init()
    finally:
        GPIO.cleanup()
