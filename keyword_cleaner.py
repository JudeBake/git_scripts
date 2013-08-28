#!/usr/bin/env python

# This script is used to clean source file from git repository in order to
# include the "last change on" date, "last change by" author, and the revison
# number.

import sys
from subprocess import call

#constant string to look for.
DATE_STR = '&DATE&'
DATE_STR_DOXY = ' * \date'
AUTHOR_STR = '&AUTHOR&'
AUTHOR_STR_DOXY = ' * \\author'
REVISION_STR = '&REVISION&'
REVISION_STR_DOXY = ' * \\version'
MARKUP_STR = '&'

print 'Cleaning file: ' + sys.argv[1] + '.'

#reading the file
fileToClean = open(sys.argv[1], "r")
lineList = fileToClean.readlines();
fileToClean.close()

#find the keyword and clean them
idx = 0
for item in lineList:
    #clean the date when found
    if not item.find(DATE_STR_DOXY) == -1 and not item.find(MARKUP_STR) == -1:
        print 'Cleaning date of last change.'
        firstMarkup = item.find(MARKUP_STR)
        strToClean = item[firstMarkup:]
        lineList[idx] = item.replace(strToClean, DATE_STR + '\n')
    #clean the author when found
    if not item.find(AUTHOR_STR_DOXY) == -1 and not item.find(MARKUP_STR) == -1:
        print 'Cleaning author of last change'
        firstMarkup = item.find(MARKUP_STR)
        strToClean = item[firstMarkup:]
        lineList[idx] = item.replace(strToClean, AUTHOR_STR + '\n')
    #clean the revision when found
    if not item.find(REVISION_STR_DOXY) == -1 and not item.find(MARKUP_STR) == -1:
        print 'Cleaning the revision'
        firstMarkup = item.find(MARKUP_STR)
        strToClean = item[firstMarkup:]
        lineList[idx] = item.replace(strToClean, REVISION_STR + '\n')
    idx = idx + 1

#clean the file
fileToClean = open(sys.argv[1], "w")
fileToClean.writelines(lineList)
fileToClean.close()

print sys.argv[1] + ' cleaning finished'        

