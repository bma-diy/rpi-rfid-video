#!/usr/bin/env python
from random import randint
import time
import subprocess
import os
import logging
import random
import glob
import RPi.GPIO as GPIO
from pirc522 import RFID


# initialize GPIO buttons
GPIO.setmode(GPIO.BOARD)
button1_pin = 12
button2_pin = 7

def playmovie(video, loop = 0):

	"""plays a video."""

	global myprocess
	global directory

	logging.debug('playmovie: linux: omxplayer %s' % video)

	proccount = isplaying()

	if proccount == 1 or proccount == 0:

		logging.debug('playmovie: No videos playing, so play video')

	else:

		logging.debug('playmovie: Video already playing, so quit current video, then play')
		myprocess.communicate(b"q")
		
	if loop == 0:
		myprocess = subprocess.Popen(['omxplayer',directory + video],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
	
	else:
		myprocess = subprocess.Popen(['omxplayer','--loop',directory + video],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
	
	time.sleep(1)

def isplaying():

		"""check if omxplayer is running
		if the value returned is a 1 or 0, omxplayer is NOT playing a video
		if the value returned is a 2, omxplayer is playing a video"""

		processname = 'omxplayer'
		tmp = os.popen("ps -Af").read()
		proccount = tmp.count(processname)

		logging.debug("isplaying: proccount: {}".format(proccount))

		return proccount

def playmenu():

		"""This will play an information video at the start of the script. When there are no videos playing, the information video will play.
		"""
		logging.debug('playmenu: No videos playing, play menu')

		menuvid = "menu1.mp4"

		# # if you want to have more than one menu video that takes turns, uncomment the next 3 lines
		#selectmenu = randint(1,2)
		#if selectmenu == 1: menuvid = "menu1.mp4"
		#elif selectmenu == 2: menuvid = "menu2.mp4"

		playmovie(menuvid,1)

def scan_card():
	# this code is complex and handles the rfid tag scanning.
	(error, tag_type) = rdr.request()

	if not error:

		(error, uid) = rdr.anticoll()
		if not error:

			idno = uid_to_num(uid)

			# Select Tag is required before Auth
			if not rdr.select_tag(uid):
				# Auth for block 10 (block 2 of sector 2) using default shipping key A
				if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
				# This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
					data = []    
					text_read = ''      

					block8 = rdr.read(8)[1]
					block9 = rdr.read(9)[1]
					block10 = rdr.read(10)[1]

					#print("Reading block 8: " + str(block8))
					if block8:

						data += block8

					if block9:

						data += block9

					if block10:

						data += block10

					#print("DATA: " + str(data))

					if data:
						text_read = ''.join(chr(i) for i in data)
						
					# Always stop crypto1 when done working
					rdr.stop_crypto()

					return True, idno, text_read

	else:

		return False, long(50), None

def uid_to_num(uid):
	n = 0
	for i in range(0, 5):
		n = n * 256 + uid[i]
	return n

#program start

rdr = RFID()

logging.basicConfig(level=logging.INFO)

directory = '/media/pi/BILLYUSB1/'

buttonmovie1 = 'video1.avi'
buttonmovie2 = 'video2.mp4'

logging.info("Begin Player")

GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True: 

		proccount = isplaying()
		logging.debug(str(proccount) + " ****************************")
		if proccount == 1 or proccount == 0:
			logging.debug("Main: Play Menu")
			current_movie_id = long(10)
			idnum = long(11)
			movie_name = 'menu_playing'
			
			playmenu()

		## Button 1
		logging.debug("**************************** BUTTON 1")
		if GPIO.input(button1_pin) == 0:
			logging.debug("Button 1 Pressed")
			idnum = long(12)
			movie_name = buttonmovie1

		## Button 2
		logging.debug("**************************** BUTTON 2")
		if GPIO.input(button2_pin) == 0:
			logging.debug("Button 2 Pressed")
			idnum = long(13)
			movie_name = buttonmovie2

		## RFID Input
		logging.debug("SCAN CARD START ****************************")
		try:

			scanned, idnum_temp, text_temp = scan_card()

			if scanned:

				idnum = idnum_temp
				movie_name = text_temp

		except TypeError:

			logging.warning("SCAN ERROR, Continue")


		logging.debug("ID: %s" % idnum)
		logging.debug("Movie Name: %s" % movie_name)

		movie_name = movie_name.rstrip()

		if current_movie_id != idnum:

			logging.debug('New Movie')
			# This is a check in place to prevent omxplayer from restarting video if ID is left over the reader.
			# Better to use idnum than movie_name as there can be a problem reading movie_name occasionally
			
			if movie_name.endswith(('.mp4', '.avi', '.m4v','.mkv')):
				current_movie_id = idnum 	#we set this here instead of above bc it may mess up on first read
				logging.info("playing: omxplayer %s" % movie_name)
				playmovie(movie_name)


except KeyboardInterrupt:
	GPIO.cleanup()
	rdr.cleanup()
	print("\nAll Done")

