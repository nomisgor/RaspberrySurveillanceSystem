		
#!/usr/bin/python
import sys
from threading import Thread
import time
import RPi.GPIO as GPIO

class LedManager(Thread):
	#constructeur
	def __init__(self, mainClass):
		#constructeur du pere
		Thread.__init__(self)

		#recuperation de l'instance de la classe mere
		self.mainClass = mainClass
		self.loop = True

		#initialisation du port d'ecriture : 7
		self.led = 7

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.led, GPIO.OUT)
		GPIO.output(self.led, GPIO.LOW)

	def run(self):
		while self.loop:
			GPIO.output(self.led, GPIO.HIGH)
			time.sleep(1.0)
			GPIO.output(self.led, GPIO.LOW)
			time.sleep(1.0)

		GPIO.output(self.led, GPIO.HIGH)

	def stopThread(self):
		GPIO.cleanup()
		self.loop = False
