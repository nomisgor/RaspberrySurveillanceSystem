#!/usr/bin/python
import mailFunction as mail
import DoorManager as dm
import LedManager as lm
import StopButtonManager as sbm
import time
import Camera as cam

class AlarmManager():

	#constructeur
	def __init__(self):

		"""		
		if mail.sendComplexMail("/home/pi/Desktop/test.txt") == 0 :
			print("mail sended.");
		else :
			print("problem durring mail sending");
		"""
		self.camera = cam.Camera()

		while True :
			self.security = 0
			#check for init button
			self.threadButton = sbm.StopButtonManager(self)
			self.threadButton.start()

			print("System standing by")

			while self.security != 1 :
				time.sleep(1.0)

			print("Launching system...")
			#launching system
			self.mainLoop = 1

			#lancement des threads
			self.threadDoor = dm.DoorManager(self)
			self.threadDoor.start()

			self.threadLed = lm.LedManager(self)
			self.threadLed.start()

			print("System online")

			#loop
			while self.mainLoop != 0 :
				#print("- 0 : Stand by")
				#self.mainLoop  = input("")
				time.sleep(1.0)

			print("System shutdown")
			
			self.stopThread(self.threadDoor)
			self.stopThread(self.threadLed)

		
	#appele quand le contact de porte s'ouvre
	def openDoor(self): 
		print("Porte ouverte !")
		self.camera.takePictures(1)

	#appele quand on veut shutdown l'alarme
	def stopThread(self, thread): 
		thread.stopThread()
		thread.join()

	#appele quand on ouvre/ferme le circuit d'arret
	def stopButton(self, value): 
		self.mainLoop = value
		self.security = value
		


main = AlarmManager()
