#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()


try:
	while True:

		id, text = reader.read()
		print(id)
		print(text)
		print(len(text))
		print(list(text))	 		
		print('finished')
except KeyboardInterrupt:
	GPIO.cleanup()
