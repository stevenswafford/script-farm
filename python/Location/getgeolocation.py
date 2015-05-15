import re
import sys
import urllib2
import BeautifulSoup

print"    _             _____ _____      _ "
print"   / \    _______|_   _|___ /  ___| |__ "
print"  / _ \  |_  /_  / | |   |_ \ / __| '_ \ "
print" / ___ \  / / / /  | |  ___) | (__| | | | "
print"/_/   \_\/___/___| |_| |____/ \___|_| |_| "
print""
print "It is all fun and games until someone gets hacked!"
print "---------------------------------------------------"
print""

usage = "Run the script: ./geolocate.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

if len(sys.argv) > 1:
    ipaddr = sys.argv[1]

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
html_page = urllib2.urlopen(geody).read()
soup = BeautifulSoup.BeautifulSoup(html_page)

# Filter paragraph containing geolocation info.
paragraph = soup('p')[3]

# Remove html tags using regex.
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print geo_txt[32:].strip()