import os
import sys
from termcolor import colored

def winLP():
	msg = '''

1. Going to have to use Kali live to get/change login page for windows
2. then open file explorer, and click on file system to open it
3. right click on an empty spot in this folder and open it in terminal.
4. proceed by typing, "cd /Windows/System32/config/"
5. now you are in the directory where the password is located, to view all existing users on the computer type out, "chntpw -l SAM"
6. once you choose a users password to remove, type out the following, "chntpw -u {user_account} SAM"
7. there will be several options to choose from after that, just select "1" (clear user password)
8. then press "q" to quit, and press "y" to save changes

	'''
	print(colored(msg, 'yellow'))
