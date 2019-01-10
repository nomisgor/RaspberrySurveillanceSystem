#!/usr/bin/python
import picamera
from datetime import datetime, timedelta
import os
import subprocess

class Camera():
	def takePictures(self, number):
		if not os.path.exists("Pictures") :
			proc = subprocess.Popen(["mkdir", "Pictures"])
			proc.wait()
		camera = picamera.PiCamera()
		camera.resolution = (1024, 768)
		for x in range (0,number):
			fileName = "Pictures/" + str(datetime.now() + timedelta(hours=1)) + ".jpg"
			camera.capture(fileName)
			print fileName + " saved"

		camera.close()
