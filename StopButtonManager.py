#!/usr/bin/python
import sys
from threading import Thread
import time
import RPi.GPIO as GPIO

class StopButtonManager(Thread):
	#constructeur
	def __init__(self, mainClass):
		#constructeur du pere
		Thread.__init__(self)

		#recuperation de l'instance de la classe mere
		self.mainClass = mainClass
		self.loop = True

		#initialisation du port d'ecoute : 16
		GPIO.setmode(GPIO.BOARD)
		self.pin = 18
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def run(self):
		previousState = -1

		while self.loop:
			if GPIO.input(self.pin) != previousState:
				previousState = GPIO.input(self.pin)
				self.mainClass.stopButton(previousState)

			time.sleep(1.0)

	def stopThread(self):
		GPIO.cleanup()
		self.loop = False
