#!/usr/bin/env python3

import webbrowser, sys, datetime

a_website = "https://mail.google.com/mail/ca/u/0/#inbox"

# last param is: update_tryorder
# update_tryorder > 0 means: append the new registered browser type into _tryorder
# update_tryorder < 0 means: insert before first element of _tryorder instead of appending
#webbrowser.register('mychrome', None, webbrowser.('Google Chrome'), -1)
#webbrowser.get(Chrome('google-chrome'))

chrome_path = '/usr/bin/google-chrome %s'
output = webbrowser.get(chrome_path).open_new_tab(a_website)
didItWork = "Failed to run"
if output:
	didItWork = "Window opened."
logFile = open('/home/dev/automation/logFile.txt', 'a')
dt = datetime.datetime.now()
logFile.write(str(dt.strftime('%Y%m%d_%H%M')) + ': was run succesfully.\nOutput: '+ didItWork +'\n\n')