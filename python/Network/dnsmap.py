#!/usr/bin/env python

# Script Name	: dnsmap.py
# Author		: Steven Swafford
# Created		: April 2015
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Maps DNS from a given domain.

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

import socket
import sys

domain = raw_input("Enter domain: ")
 
try:
    ip = socket.gethostbyname(domain)
 
except socket.gaierror:
    print "Invalid Domain: " + domain
    sys.exit()
print "DNS: " + ip