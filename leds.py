#!/usr/bin/env python

import RPi.GPIO as GPIO

DEBUG = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def init():
    
    if newmails > NEWMAIL_OFFSET:
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
    else:
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)

    time.sleep(MAIL_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        init()
    finally:
        GPIO.cleanup()
