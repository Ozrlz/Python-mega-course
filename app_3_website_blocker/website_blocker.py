# -*- coding: utf-8 -*-

from os import name as so_type
from datetime import datetime as dt
from time import sleep 
from re import split

#CONSTANTS
HOSTS_PATH_FILE = '/etc/hosts' if so_type == 'posix' else r"C:\Windows\System32\drivers\etc\hosts" if so_type == 'nt' else ''
REDIRECT = '127.0.0.1'
#HOSTS_PATH_FILE = 'hosts'
WORKING_HOUR_BEGIN = 19
WORKING_HOUR_END = 20
SLEEP_MINUTES = 5
TMP_FILE = 'super_secret_hosts_tmp_file'


website_list = ['www.facebook.com', 'facebook.com']

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, WORKING_HOUR_BEGIN) < dt.now() < dt(
		dt.now().year, dt.now().month, dt.now().day, WORKING_HOUR_END):
		print ('Working hours')
		with open(HOSTS_PATH_FILE, 'r+') as hosts_file:
			content = hosts_file.read()
			for website in website_list:
				if website in content:
					print ("smn")
					pass
				else:
					print ('nel')
					nameserver = REDIRECT + '\t' + website + '\n'
					print (nameserver)
					hosts_file.write(nameserver)
	else:
		with open(HOSTS_PATH_FILE, 'r+') as hosts_file:
			content = hosts_file.readlines()
			hosts_file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					hosts_file.write(line)
			hosts_file.truncate()
		print ('No WORKING_HOURs')
	sleep(60*SLEEP_MINUTES)
