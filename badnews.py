import os
import sys
from termcolor import colored
import time

from tuts import winLogin
from tuts import captivePortal
from tuts import pmkid
from tuts import pmkid2
from tuts import imgEmbed
'''
from tuts import 
from tuts import 
from tuts import 
from tuts import 
'''


options = '''

[brute]force
[bypass]
[crack]
[wifi]
[embed]

[quit]

'''
bpMenu = '''

[windows] login page

'''
wifiMenu = '''

[captive] portal - use to collect social media credentials
[pmkid] attack (using hcxdumptool)
[pmkid2] attack (using bettercap)
'''
bruteMenu = '''

[http-post]-form
[ftp]
[ssh]
[telnet]
[rdp]
[smtp]
[zip]
[7z]
[pdf]
[keepass]


'''
embedMenu = '''

[payload] embedded image

'''



def spoon_fed():
	sel = ''
	while sel != 'quit':
		print(colored(options, 'magenta'))
		sel = input('> ')

#	BRUTE
		'''
		if sel == 'brute':
			print(colored(bruteMenu, 'magenta'))
			run = input('> ')
			if run == 'http-post':
				
			elif run == 'ftp':
				
			elif run == 'ssh':
				
			elif run == 'telnet':
				
			elif run == 'rdp':
				
			elif run == 'smtp':
				
			elif run == 'zip':
				
			elif run == '7z':
				
			elif run == 'pdf':
				
			elif run == 'keepass':
				
		'''

#	BYPASS
		if sel == 'bypass':
			print(colored(bpMenu, 'magenta'))
			run = input('> ')
			if run == 'windows':
				winLogin.winLP()
#	CRACK
		elif sel == 'crack':
			print('Under Construction')

#	WIFI
		elif sel == 'wifi':
			print(colored(wifiMenu, 'green'))
			run = input('> ')
			if run == 'captive':
				captivePortal.capPort()
			elif run == 'pmkid':
				pmkid.attack()
			elif run == 'pmkid2':
				pmkid2.psk()

			else:
				print('Invalid Input')

		elif sel == 'embed':
			print(colored(embedMenu, 'green'))
			run = input('> ')
			if run == 'payload':
				imgEmbed.mal()
			else:
				print(colored('Error Occured', 'red'))



		elif sel == 'quit':
			print(colored('~~ GOODBYE  ~~', 'cyan'))

		else:
			print(colored('ERROR OCCURED', 'red'))



spoon_fed()
