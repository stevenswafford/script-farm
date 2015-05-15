#! /usr/bin/python3
# -*- coding: utf-8 -*-

""" Text to Sorted with no repeated elements Word-List creator in Python 3.

BY:
      ____              _    _             __  __            
     / ___| _ __   __ _| | _(_)_ __   __ _|  \/  | __ ___  __
     \___ \| '_ \ / _` | |/ / | '_ \ / _` | |\/| |/ _` \ \/ /
      ___) | | | | (_| |   <| | | | | (_| | |  | | (_| |>  <    ____
 ____|____/|_| |_|\__,_|_|\_\_|_| |_|\__, |_|  |_|\__,_/_/\_\__/ O  \___/
<\x41\x41\x41\x41\x41\x41\x41\x41\x41|___/\x41\x41\x41\x41\x41______/   \

                 snakingmax [at] hotmail [dot] com
                   site: snakingmax.blogspot.com
"""

import sys

def delRepeated(myList):
	outputList = []
	for i in myList:
		if i not in outputList:
			outputList.append(i)
	return outputList

def makeWordList(text, wordlist):
	textFile = open ( text , 'rt')
	dump = textFile.read()
	textFile.close()
	myList = dump.split()
	myList.sort()
	myList = delRepeated(myList)
	wordPos=0
	wordListFile = open ( wordlist , 'at')
	for i in myList:
		wordListFile.write (myList[wordPos]+"\n")
		wordPos=wordPos+1
	wordListFile.close()
	return wordPos

if (__name__=="__main__" ):
	if len(sys.argv) != 3:
		print("usage:\n")
		print("text2dictsort [text.txt] [wordlist.txt]\n\n")
		print("Downloaded from: http://snakingmax.blogspot.com/")
	else:
		text = sys.argv[1];
		wordlist = sys.argv[2];
		wordListFile = open ( wordlist , 'wt')
		wordListFile.close()
		numWords = makeWordList(text, wordlist)
		print("Word-list created in: {0}\nTotal words: {1}.".format( sys.argv[2], numWords ))
