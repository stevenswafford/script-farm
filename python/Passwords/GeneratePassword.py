import string
from random import *

# Script that generates a random password."

print"    _             _____ _____      _ "
print"   / \    _______|_   _|___ /  ___| |__ "
print"  / _ \  |_  /_  / | |   |_ \ / __| '_ \ "
print" / ___ \  / / / /  | |  ___) | (__| | | | "
print"/_/   \_\/___/___| |_| |____/ \___|_| |_| "
print""
print "It is all fun and games until someone gets hacked!"
print "---------------------------------------------------"
print""

usage = "Run the script: ./generatepassword.py"

minLength = int(raw_input('Enter minimum length of password: '))
maxLength = int(raw_input('Enter maximum length of password: '))

characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters)
                   for x in range(randint(minLength, maxLength)))
print "Your password:", password
