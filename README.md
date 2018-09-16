# rpi-rfid-video
This is a a video player that scans RFID cards to play videos.

Kids love this video player.
This is a great project for folks that are new to programming. 

### You will need the following:

* Raspberry Pi 3
* RFID RC522 Kit
* RFID 13.56 MHz Cards

### Follow these instructions on setting up the RFID kit w/ your Pi: 
* [How to setup a Raspberry Pi RFID RC522 Chip - Pi My Life Up](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
* [RFID (RC522) - piddlerintheroot |  piddlerintheroot](https://www.piddlerintheroot.com/rfid-rc522-raspberry-pi/)

### The Raspberry Pi 3 has a video player preinstalled called: OMXPlayer
[OMXPlayer: An accelerated command line media player - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md)

### Scripts
* bplay.py - the script that actually scans the card and plays the video
* read.py - a simple script to test reading your script
* write.py - a simple script to write the text portion of the RFID card

You will not be able to have multiple scripts using the RFID sensor running at the same time, so only run one at a time.

You can have your code execute at runtime by adding it to the /etc/rc.local file

### Youtube Video Demo
https://youtu.be/92qb6oVzuHA
