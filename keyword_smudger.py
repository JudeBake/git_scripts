# This script is used to smudge source file from git repository in order to
# include the "last change on" date, "last change by" author, and the revison
# number.

import sys
import subprocess

#constant string to look for.
DATE_STR " * \date Last change on:"
AUTHOR_STR " * \author Last change by:"
REVISION_STR " * \version Revision:"

#open the file
fileToSmudge = open(sys.agrv, "r")
linelist = fileToSmudge.readlines()
fileToSmudge.close()


