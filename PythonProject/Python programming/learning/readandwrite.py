# This program writes text into files
from sys import argv
script = argv

targetfile = input("Enter the name the file to be written : ")
inputtext = input("Enter the text to be added : ")

print(f"The file name is : {targetfile}")
print(f"The Text to be added is : {inputtext}")

# Create an object
#Call write and read method
writefile = open(targetfile, 'w+')
writefile.write(inputtext)
writefile.close()
print(f"Writing into file {targetfile} has been completed!")
print("=============================")

readfile = open(targetfile)
print(f"The contents in {targetfile} is : \n")

print(readfile.read())
readfile.close()
