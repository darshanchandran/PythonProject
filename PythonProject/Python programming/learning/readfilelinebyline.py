# This program reads the file line by line
targetfile = input("Enter the file to be read : ")

print("The Whole content is as follows : ")
readfile = open(targetfile)
print(readfile.read())
readfile.close()

print("============End of file===========")

# Read the file line by line , reads two line
print("======Read two line=======")
readfile = open(targetfile)
print(readfile.readline())
print(readfile.readline())
readfile.close()

# Read a file with function implemented
print("===== Reading with Function==========")

def readfilefn(targetfile1):
    readfile = open(targetfile1)
    print(readfile.readline())
    readfile.close()

readfilefn(targetfile)

# Get the number of lines to be printed
getline = input("Enter the number of Lines to be printed : ")
getline = int(getline)
def readfilelinefn(getline,targetfile):
    readfile = open(targetfile)
    i = 1
    while (i <= getline):
        print(readfile.readline())
        i = i + 1

readfilelinefn(getline,targetfile)

# Read all the files with two arguments

def readlinewitharg(linecount,targetfile):
    #readfile = open(targetfile)
    print(linecount,readfileout.readline())

readfileout = open(targetfile)
i = 1
i = int(i)

readlinewitharg(i,readfileout)

i = i + 1
readlinewitharg(i,readfileout)

i = i + 1
readlinewitharg(i,readfileout)
