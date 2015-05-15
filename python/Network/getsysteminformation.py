#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:		   systemInformation.py
# Version:	   1.1
# Author:	   Jordan Rowles
# Created:	   21/02/2014
# Copyright (c) Jordan Rowles 2014
# GNU General Public License Version 3 or Later
#-------------------------------------------------------------------------------
import os, sys, platform
import socket, subprocess
import formatDate

sep = '  ' # 2 Spaces

class argumentError(ValueError):
      'Error relating to arguments when calling functions'

def getMachineInfoDict():
	'Gets all information inside a dictionary'
	infoDict = {
		'OS Name:'             : getOSName(),
		'Platform (Bit):'      : getPlatform(),
		'Win Reg Ver:'         : registryVerWin(),
		'Win Version:'         : getWindowsInformation(),
		'Architecture:'        : getArchitecture(),
		'Machine Type:'        : getMachineType(),
		'Network Name:'        : getNetworkName(),
		'Machine Platform:'    : getMachinePlatform(),
		'Processor:'           : processorInformation(),
		'Operating Sys:'       : getOperatingSystem(),
		'Platform Release:'    : platformRelease(),
		'Machine Info:'        : returnMachineInfo(),
		'Win Version:'         : getWindowsVersion(),
		'Mac Version:'         : getMacOSVersion(),
		'Unix Version:'        : getUnixVersion(),
		'Python Version'       : pythonVersion(),
		'Python/C API Ver:'    : pythonCAPIVersion(),
		'Version Information:' : versionInformation()}
	return infoDict
def getInfoDictKeys():
	infoDictKeys = infoDict.keys()
	return infoDictKeys
def getInfoDictVals():
	infoDictVals = infoDict.values()
	return infoDictVals

def getIPv4():
    'Returns local IP (v4)'
    IP = socket.gethostbyname(socket.gethostname())
    return IP

def getInformationFromCMD():
    '''Uses subprocess module to enter ipconfig into cmd, parse the string
       and return it as a key-value dictionary.
    '''
    process = subprocess.Popen('ipconfig /all', stdout=subprocess.PIPE, shell=True)
    output = process.communicate()
    output = output[0]
    # Parse and Format into dictionary
    result = {}
    for eachRow in output.split('\n'):
        if ': ' in eachRow:
           key, value = eachRow.split(': ')
           result[key.strip(' .')] = value.strip()
    return result

## SOME RETURNS NEED TO BE PROPERLY FORMATTED TO STRINGS
## I.E. FROM TUPLES AND LISTS
def getOSName(formStr=0):
	'''OS Names: posix, nt, os2, ce, java or rescos
	   Args:
            0 - Unformatted (string)
            1 - Capitalised (may not work for os2?)
            2 - Returns formatted for display (string)
            3+ - Raises argumentError exception
	'''
	if formStr == 0: string = os.name
	elif formStr == 1: string = os.name.upper()
	elif formStr == 2: string = 'OS Name: %s' % os.name
	else: raise argumentError('Enter integer from 0-2')
	return string

def getPlatform(formStr=False):
	'atheos, riscos, os2emx, os2, darwin, cygwin, win32 or linux2'
	if formStr == False: string = sys.platform
	else: string = 'Platform (bit): %s' % sys.platform
	return string

def registryVerWin(formStr=False):
	'Windows registry keys version'
	if formStr == False: string = sys.winver
	else: string = 'Win Reg Version: %s' % sys.winver
	return string

def getWindowsInformation(formStr=0):
    '''Gets Windows information: Major, Minor, Build, Platform and SP.
       Args:
            0 - Unformatted (function and tuple) (default)
            1 - Returns formatted for dispaly (string)
            2 - Returns formatted without label (string)
            3+ - Raises argumentError exception'''
    if formStr == 0: string = sys.getwindowsversion()
    elif formStr == 1: string = 'Win Info: %s' % formatWindowsInformation()
    elif formStr == 2: string = formatWindowsInformation()
    else: raise argumentError('Enter integer from 0-2')
    return string

def getArchitecture(formStr=0):
    '''Sets system architecture (bit, linkage/type).
       Args:
            0 - Unformatted (tuple) (default)
            1 - Returns just the bit (string)
            2 - Returns just the linkage (string)
            3 - Fully formatted for display (string)
            4 - Returns comma seperated bit and linkage
            5+ - Raises argumentError exception.'''
    architecture = platform.architecture()
    if formStr == 0: string = architecture #Unformatted
    elif formStr == 1: string = architecture[0] #Bit
    elif formStr == 2: string = architecture[1] #Linkage
    elif formStr == 3: string = 'Architecture: %s, %s' % (architecture[0],
         architecture[1])
    elif formStr == 4: string = '%s, %s' % (architecture[0], architecture[1])
    else: raise argumentError('Enter integer from 0-3')
    return string

def getMachineType(formStr=False):
	'Returns machine type (i386, x86)'
	if formStr == False: string = platform.machine()
	else: string =  'Machine Type: %s' % platform.machine()
	return string

def getNetworkName(formStr=False):
	'Gets machines name on a network (MK02514)'
	if formStr == False: string = platform.node()
	else: string = 'Network Name: %s' % platform.node()
	return string

def getMachinePlatform(formStr=False):
	'Gets full machine information Windows-8-6.2.9200'
	if formStr == False: string = platform.platform()
	else: string = 'Machine Platform: %s' % platform.platform()
	return string

def processorInformation(formStr=False):
	'Gets processor information'
	if formStr == False: string = platform.processor()
	else: string = 'Processor: %s' % platform.processor()
	return string

def getOperatingSystem(formStr=False):
	'Gets OS name'
	if formStr == False: string = platform.system()
	else: string = 'Operating Sys: %s' % platform.system()
	return string

def platformRelease(formStr=False):
	'Gets the OS version'
	if formStr == False: string = platform.release()
	else: string = 'Platform Release: %s' % platform.release()
	return string

def returnMachineInfo(formStr=False):
	'Returns a tuple of: OS, network name, OS version, @, processor info'
	if formStr == False: string = platform.uname()
	else: string = 'Machine Info: %s' % platform.uname()
	return string

def getWindowsVersion(formStr=False):
	'Get Windows Platform. Specific.'
	if formStr == False: string = platform.win32_ver()
	else: string = 'Win Version: %s' % platform.win32_ver()
	return string

def getMacOSVersion(formStr=False):
	'Gets Mac Platform. Specific'
	if formStr == False: string = platform.mac_ver()
	else: string = 'Mac Version: %s' % platform.mac_ver()
	return string

def getUnixVersion(formStr=False):
	'Get Unix Platform. Specific'
	if formStr == False: string = platform.dist()
	else: string = 'Unix Version: %s' % platform.dist()
	return string

	# -- PYTHON INFOMRATION --
def pythonVersion(formStr=False):
	'Version of Python'
	if formStr == False: string = sys.version
	else: string = 'Python Version: %s' % sys.version
	return string

def pythonCAPIVersion(formStr=False):
	'Python/C Interpreter API Version'
	if formStr == False: string = sys.api_version
	else: string  = 'Python/C Api Ver: %s' % sys.api_version
	return string

def versionInformation(formStr=False):
	'Python version as named tuple - NEEDS FORMATTING'
	pass
	if formStr == False:
		return sys.version_info
	else:
		pass
		#Format Here

def getFileSystemEncoding(formStr=False):
    'Gets the character encoding for the local file system'
    encoding = sys.getfilesystemencoding()
    if formStr == False: encoding = encoding
    elif formStr == True: encoding = encoding.upper()
    return encoding

# Format Machine Information
def formatWindowsInformation(build=False):
	'Formats information from sys.getwindowsversion()'
	windowsInfo = getWindowsInformation()
	winMajor = windowsInfo[0] # Major Version
	winMinor = windowsInfo[1] # Minor Version
	winBuild = windowsInfo[2] # Build Number
	servicePack = windowsInfo[4] # Service Pack
	platform = windowsInfo[3] # Platform Type
	if platform == 0: platType = '3.1' # 0=Win3.1
	if platform == 1: platType = '95/98/ME' # 1=95/98/ME
	if platform == 2: platType = 'NT' # 2=NT/2000/XP/x64
	if platform == 3: platType = 'CE' # 3 = CE
	winNum = getWindowsVersion()[0]
	if build == False:
		 formInfo = 'Windows %s %s %i.%i' % (winNum, platType, winMajor, winMinor)
	else:
		 formInfo = 'Windows %s %s %i.%i %i' % (winNum, platType, winMajor, winMinor, winBuild)
	return formInfo

def formatEnvironmentInformation(formStr=0):
    'Formats information from os.environ'
    environInfo = os.environ
    userName = environInfo['USERNAME']
    compName = environInfo['COMPUTERNAME']
    domainNa = environInfo['USERDOMAIN']
    userProf = environInfo['USERPROFILE']
    if formStr == 1: string = '%s is logged in at %s on %s' % (userName, compName, domainNa)
    if formStr == 2: string = userName
    if formStr == 3: string = compName
    if formStr == 4: string = domainNa
    if formStr == 5: string = userProf
    if formStr == 0: string = [userName, compName, domainNa, userProf]
    return string

# Write Information To File
def fileName():
	'Generate filename for information'
	filename = '%s.txt' % getNetworkName()
	return filename

def writeInfoFile():
	'Write information to file'
	file = open(fileName(), 'w')
	file.write('OS Name: ', getOSName())
	file.close()

def returnInformation():
    'Returns all information in the syntax - Name: (sep) value()'
    print '       OS Name:%s%s, %s' % (sep, getOSName(1), getOperatingSystem())
    print 'Platform (bit):%s%s' % (sep, getPlatform())
    print '      Win Info:%s%s' % (sep, getWindowsInformation(2))
    print '  Architecture:%s%s' % (sep, getArchitecture(4))
    print 'Processor Type:%s%s' % (sep, getMachineType())
    print '  Network Name:%s%s' % (sep, getNetworkName())
    print '     Processor:%s%s' % (sep, processorInformation())
    print '    IP Address:%s%s' % (sep, getIPv4())
    print '     User Name:%s%s' % (sep, formatEnvironmentInformation(2))
    print '        Domian:%s%s' % (sep, formatEnvironmentInformation(4))

# [Script] Call returnInformation() on execution
def getBasicInfo():
    returnInformation()

if __name__ == '__main__':
    pass
    #getBasicInfo()