import os
import sys
from termcolor import colored

def http():
	target = input('Website URL:\n> ')
	ul = input('Path To A Username/Email Wordlist:\n> ')
	pl = input('Path To A Password Wordlist:\n> ')
	user = input('When You Inspect Page, What Is The Username Placeholder Called:\n> ')
	passw = input('When You Inspect The Page, What Is The Password Placeholder Called:\n> ')
	submit = input('When You Inspect The Page, What Is The Submit Button Called:\n> ')
	fail = input('When You Put In The Incorrect Password, Paste In The Message That Comes Up:\n> ')

	try:
		command = f'hydra -L {ul} -P {pl} {target} http-post-form 

	except:
		command = f'hydra -L {ul} -P {pl} domain.htb http-post-form "
