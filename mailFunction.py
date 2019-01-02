#!/usr/bin/python
def sendComplexMail(filePath):
	#import pour la gestion des mails
	import smtplib
	from email.MIMEMultipart import MIMEMultipart
	from email.MIMEText import MIMEText
	from email.MIMEBase import MIMEBase
	from email import encoders
	
	#import pour tester la presence du fichier
	import os.path

	if not os.path.isfile(filePath) :
		return -1;

	mustSendMail = True;
 
	fromaddr = "nomisgor0@gmail.com"
	toaddr = "simgorecki@gmail.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Intrusion detected"
 	
	body = "Text de mon email"
 
	msg.attach(MIMEText(body, 'plain'))
 
	filename = "NomDeMonFicher.txt"
	attachment = open(filePath, "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "PAULINE002106")
	text = msg.as_string()
	if mustSendMail == True :
		server.sendmail(fromaddr, toaddr, text)
	server.quit()
	return 0;


def sendSimpleMail():
	import smtplib
	
	myMailAdress = "nomisgor0@gmail.com"
	myMailPassword = "PAULINE002106"
	dstMail = "simgorecki@gmail.com"
	
 	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(myMailAdress, myMailPassword)
 	msg = "YOUR MESSAGE!"
	server.sendmail(myMailAdress, dstMail, msg)
	server.quit()


def myFunction(nom, prenom):
	for x in xrange(1, 10):
		print(x);
		print("nom : "+nom);
		print("prenom : "+prenom);
		print("  ");
