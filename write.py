#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

print('Scan Card')

try:

    while True:

        text = raw_input('New data:')

        if len(text) > 48:

            text = raw_input('Data was too long, shorten it and type it here:')

        print("Now place your tag to write")

        reader.write(text)
        print("Written")


except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nClean Exit")
