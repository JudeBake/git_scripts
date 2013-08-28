#!/usr/bin/env python

# This script is used to smudge source file from git repository in order to
# include the "last change on" date, "last change by" author, and the revison
# number.

import sys
import subprocess

#constant string to look for.
DATE_STR = '&DATE&'
AUTHOR_STR = '&AUTHOR&'
REVISION_STR = '&REVISION&'
MARKUP_STR = '&'

print 'Smudging file: ' + sys.argv[1] + '.'

#open the file
fileToSmudge = open(sys.argv[1], "r")
lineList = fileToSmudge.readlines()
fileToSmudge.close()

#find the keyword and smudge them with the desired values
idx = 0
for item in lineList:
    #smudge the date when found
    if not item.find(DATE_STR) == -1:
        #getting the date of the last commit
        lastChangeDate = subprocess.call("/usr/bin/git log --pretty=format:\"%ad\"")
        print lastChangeDate
        lineList[idx] = item.replace(DATE_STR, '&abcd&')
        print 'Keyword ' + DATE_STR + ' found and smudge.'
    #smudge the author when found
    if not item.find(AUTHOR_STR) == -1:
        lineList[idx] = item.replace(AUTHOR_STR, '&abcd&')
        print 'Keyword ' + AUTHOR_STR + ' found and smudge.'
    #smudge the revision when found
    if not item.find(REVISION_STR) == -1:
        lineList[idx] = item.replace(REVISION_STR, '&abcd&')
        print 'Keyword ' + REVISION_STR + ' found and smudge.'
    idx = idx + 1

#smudge the file
fileToSmudge = open(sys.argv[1], "w")
fileToSmudge.writelines(lineList)
fileToSmudge.close()

print sys.argv[1] + ' smudging finished.'



