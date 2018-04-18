# This script copies the contents from one file to another

import sys

fromfile = input("Enter the File from which the contents needs to be copied : ")
tofile = input("Enter the File to which the contest needs to  be copied : ")

# Assign object to read the files

readfile = open(fromfile , 'r+')
data = readfile.read()
readfile.close()

writefile = open(tofile , 'w+')
writefile.write(data)
writefile.close()
