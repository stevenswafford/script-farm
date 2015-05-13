#!/bin/bash

# Script Name	: dnsmap.py
# Author		: Steven Swafford
# Created		: April 2015
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Download files using curl.

# It is all fun and games until someone gets hacked!
#          _                      _
#   _     /||       .   .        ||\     _
#  ( }    \||D    '   '     '   C||/    { % 
# | /\__,=_[_]   '  .   . '       [_]_=,__/\ |
# |_\_  |----|                    |----|  _/_|
# |  |/ |    |                    |    | \|  |
# |  /_ |    |                    |    | _\  |

echo "Enter the name of your flat file: "
read input_variable
echo "You entered: $input_variable"

#create urls variable array
declare urls=( `cat "$input_variable" `)

#Download files from URL list
for m in "${urls[@]}"
	do curl -O "$m"
done