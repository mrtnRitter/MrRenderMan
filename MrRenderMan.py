# -*- coding: utf-8 -*-

# import stuff...
import ctypes
import os, sys
from sys import argv, executable
import subprocess
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE
import time
from tkinter import Tk, filedialog
from tkinter.filedialog import askopenfilename

#set console width and heigth
os.system("mode con cols=70 lines=40")

#clear console
clear = lambda: os.system('cls')
clear()
	
#define variable, has the same value as cols, this is all just to center the text
consolewidth = 70

# behave as worker
# check if there is an argument to the script call and if, use this as filein
if len(sys.argv) == 2:
	ctypes.windll.kernel32.SetConsoleTitleW("Mr. Render Man: Worker")
	
	filein = sys.argv[1]
			
	os.chdir ("C:\Program Files\Adobe\Adobe After Effects CC 2018\Support Files")

	#error and render switches
	rrender = 1
	
	while rrender == 1:
		rrender = 0
		#start aerender, outs and errors go to pipe for further analysing	
		aerender = subprocess.Popen(["aerender.exe", "-project", filein],stdout=PIPE, stderr=subprocess.STDOUT)
	
		# poll is true as long as aerender is running
		while aerender.poll() == None:
			# read out pipe line by line
			aeoutmsg = aerender.stdout.readline()
			#replace unicode escapes for better look
			aeoutmsg = aeoutmsg.replace(b"\x1b[1m\x1b[0m", b"")
			aeoutmsg = aeoutmsg.replace(b"\r\n", b"")
			# print pipe in console, convert bytestring to unicode for umlauts
			print (aeoutmsg.decode('iso8859-1'))
			# analysis: if the word fehler appears, restart aerender to finish render process
			if str(aeoutmsg).find("Fehler") >= 0:
				rrender = 1		

				
#behave as caller
#input file, name is empty, and while the name is empty, script keeps asking to set input file, Tk Mainwindow is hidden and afterward destroyed to get the focus back to console		
else:
	while True:
		ctypes.windll.kernel32.SetConsoleTitleW("Mr. Render Man")
		print ("\n")
		print (str.center("*** Mr. Render Man ***", consolewidth))
		print (str.center("*** Version 1.04 ***", consolewidth))
	
		print ("\n")
		print ("Fenster schließen zum Beenden.")
		print ("\n")
	
		filein = ""
	
		while filein == "":
			input ("Enter drücken um AFX-Projekt zu öffnen ...")
			root = Tk()
			root.withdraw()
			filein = askopenfilename(filetypes=[('Adobe After Effects-Projekt','*.aep')])
		
		#if there has been an argument passed, while loop will not entered and therefor root will not be definded - catch this error event and go on
		try:
			root.destroy()
		except NameError:
			root = None
			
		print ("\n")
		print ("Folgendes Projekt wird gerendert:")
		print (filein)
		print ("\n")
			
		# auto shutdown input	
		sd = input ("Computer nach dem Rendern herunterfahren? [j/n]: ")
		print ("\n")
		
		while sd != "j" and sd != "n":
			sd = input("Bitte 'j' oder 'n' drücken! Computer nach dem Rendern herunterfahren? [j/n]: ")
			print ("\n")
		
		if sd == "j":
			print ("Automatisches Herunterfahren ist AKTIV!")	
			print ("\n")
		
		# set workers
		worker = input ("Wieviele Worker sollen gestartet werden? [1-8]: ")
			
		while worker < "1" or worker > "8":
			print ("\n")
			print ("Nein! Nein! Nein! Nein! Nein! Nein! Nein! Nein! Nein!")
			print ("\n")
			worker = input ("Wieviele Worker sollen gestartet werden? [1-8]: ")
				
		print ("\n")
		print ("Starte " + worker + " Worker ...")
		print ("\n")

		worker = int(worker)
		i = 0
		
		while i < worker:
			# check if file extension is .py or .exe... because I'm sick of changing this code all the time when ruinning pyinstaller
			exe_or_py = sys.argv[0]
			if exe_or_py.split(".")[1] == "py":
				wrk = subprocess.Popen([sys.executable, sys.argv[0], filein], creationflags=CREATE_NEW_CONSOLE)
			else:
				wrk = subprocess.Popen([sys.argv[0], filein], creationflags=CREATE_NEW_CONSOLE)
				
			print ("Worker " + str(i+1) + " gestartet.")
			print ("\n")
			i+=1
			time.sleep (30)	
		
		while wrk.poll() == None:
			print ("Rendervorgang läuft ...")
			print ("\n")
			time.sleep (30)
		
		print ("Rendervorgang abgeschlossen!")
		print ("\n")
		print ("\n")
		
		print (str.center("(C) Büro Vogel&Moritz 2017 | www.vogelmoritz.de", consolewidth))
		print ("\n")
		
		#auto shutdown exec
		if sd =="j":
			#check if another worker is running
			tasks = str(subprocess.check_output('tasklist /fo csv'))
			taskrun = tasks.find("AfterFX.com")
				
			while taskrun != -1:
				print ("Weiteren Rendervorgang entdeckt! Herunterfahren wird um 5 Minuten verzögert ...")
				print ("\n")
				time.sleep (300)
				tasks = str(subprocess.check_output('tasklist /fo csv'))
				taskrun = tasks.find("AfterFX.com")
			
			
			print ("Alle Renderaufgaben sind beendet. Computer wird in 20 Sekunden heruntergefahren.")
			print ("\n")
			os.system("shutdown /s /t 20")
			sda = input ("Herunterfahren abbrechen? [a]: ")
			
			while sda != "a":
				print ("\n")
				print ("Automatisches Herunterfahren ist noch AKTIV!")
				print ("\n")
				sda = input ("Bitte 'a' drücken um Herunterfahren abzubrechen.")
			
			if sda == "a":
				os.system("shutdown /a")
				print ("\n")
				print ("Computer wird nicht heruntergefahren.")
				print ("\n")
				print ("Fenster schließen zum Beenden")
				print ("\n")
				input ("Enter drücken um weiteres Projekt zu rendern.")
				clear()
			
		if sd == "n":		
			print ("Fenster schließen zum Beenden")
			print ("\n")
			input ("Enter drücken um weiteres Projekt zu rendern.")
			clear()
			