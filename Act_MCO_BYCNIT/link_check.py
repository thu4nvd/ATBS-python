
# Author: bnmd
# Date: 2021 Juin 11
# Structure of input Excel file: 	url,username,password,Domain,Expect,Result-check
# Script read the content of Excel file and do check the link.
# Version 1: check the link, without the credentials.

import urllib.request
import ssl
import os

# Fix ssl error
context = ssl._create_unverified_context()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'urls.txt'), "r")
f_result = open(os.path.join(__location__, 'result.txt'), "w")
for link in file:
    try:
        f_result.write(link + "/t/t" + str(urllib.request.urlopen(link, context=context).getcode()))
    except urllib.error.HTTPError as exception:
        f_result.write(link + "/t/t" + str(exception))
file.close()
f_result.close()

# Read excel file
# for each line
# 	check url()
# 		if domain()
# 		if username+password
# 		result = return()
# 	write result to the excel file.
# 	send email.

# Schedule to run the script.
# Write log file.

# schedule the send email.