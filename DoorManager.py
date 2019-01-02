#!/usr/bin/python
import sys
from threading import Thread
import time
import RPi.GPIO as GPIO

class DoorManager(Thread):
	#constructeur
	def __init__(self, mainClass):
		#constructeur du pere
		Thread.__init__(self)

		#recuperation de l'instance de la classe mere
		self.mainClass = mainClass
		self.loop = True

		#initialisation du port d'ecoute : 16
		GPIO.setmode(GPIO.BOARD)
		self.pin = 16
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def run(self):
		while self.loop:
			if GPIO.input(self.pin):
				self.mainClass.openDoor()
			time.sleep(0.1)

	def stopThread(self):
		GPIO.cleanup()
		self.loop = False
