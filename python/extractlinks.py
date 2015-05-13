#!/usr/bin/env python

# Script Name	: extractlinks.py
# Author		: Steven Swafford
# Created		: April 2014
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Extract all links from a given url

print""
print "It is all fun and games until someone gets hacked!"
print"          _                      _          "
print"   _     /||       .   .        ||\     _   "
print"  ( }    \||D    '   '     '   C||/    { %  "
print" | /\__,=_[_]   '  .   . '       [_]_=,__/\ |"
print" |_\_  |----|                    |----|  _/_|"
print" |  |/ |    |                    |    | \|  |"
print" |  /_ |    |                    |    | _\  |"
print""
print""

import sys
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup

class urlRipper(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'


def get_url():
    try:
        url = str(raw_input('Enter URL: '))
        if not url:
            raise ValueError('No URL was provided! What were you expecting?')
        else:
            print url
            process_url(url)
    except ValueError as e:
        print(e)
        exit()


def process_url(url):
    urlripper = urlRipper()
    page = urlripper.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        myUrl = tag['href']
        print "Here is what is being extract to a text file: " + myUrl
        write_results(myUrl)

# process(url)


def write_results(myUrl):
    file = open("output.txt", "a")
    file.write(myUrl + "\n")
    file.close()


# writeresults()

get_url()

# ## Done!