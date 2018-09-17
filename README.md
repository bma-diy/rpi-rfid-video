# rpi-rfid-video
This is a a video player that scans RFID cards to play videos.

Kids love this video player.
This is a great project for folks that are new to programming. 

### Youtube Video Demo
https://youtu.be/92qb6oVzuHA

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


### Extra Info

* Enable HDMI Hotplug
There may be situations where you power your Raspberry Pi before plugging in the HDMI cable and your screen may remain black. To have your Pi detect HDMI after being powered on, add these two lines to /boot/config.txt and reboot:

```
hdmi_force_hotplug=1
hdmi_drive=2
```
[Video options in config.txt - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/configuration/config-txt/video.md)

* Code execution at start up
You can have your code execute at runtime by adding it to the /etc/rc.local file
[rc.local - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)

* Hide mouse cursor by installing Unclutter
[Hide Raspberry Pi Mouse Cursor in Raspbian (Kiosk)](https://jackbarber.co.uk/blog/2017-02-16-hide-raspberry-pi-mouse-cursor-in-raspbian-kiosk)
