#!/usr/local/munki/Python.framework/Versions/Current/bin/python3
from datetime import datetime
import subprocess


user = '<USERNAME_HERE>'
passwordLastSetDate = subprocess.check_output(['/usr/bin/dscl', '.', '-readpl', '/Users/' + user, 'accountPolicyData',  'passwordLastSetTime'])
lastSetDate = str(passwordLastSetDate, 'utf-8')
lastSetDate = lastSetDate.split(' ')[1][:-2]
lastSetDate = datetime.fromtimestamp(float(lastSetDate))

# 'datetime' supports addition and subtraction between 'datetime.date' objects
# We use this here to obtain the number of days from today and the 'lastSetDate'
today = datetime.now()
passwordAge = (today - lastSetDate).days

# Output the result for the extension attribute
print(("<result>{0}</result>".format(passwordAge)))

