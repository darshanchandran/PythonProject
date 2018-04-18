# This program shows how to play with the words in a sentence

# Function to strip words from sentence

def splitword(file):
    openfile = file.open()
    splitword = openfile.split(' ')
    return splitword
