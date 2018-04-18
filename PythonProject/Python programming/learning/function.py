# This script shows how to create functions

# Single argument
def displayname(arg1):
    print(f"your name is {arg1}")

displayname('darshan')
displayname('bangalore')

# Multiple arguments
def displaynames(arg1,arg2):
    print(f"your name is {arg1} and {arg2}")

displaynames('dd','tt')

# Addition functions
def addition(arg1,arg2):
    sum = arg1 + arg2
    print(f"Sum = {sum}")

addition('4','5')
