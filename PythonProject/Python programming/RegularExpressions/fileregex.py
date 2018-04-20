# This program shows how regex can be used reading through file

import re


class Readfile(object):

    def openfile(self):
        file = input("Enter the File to be read : ")
        openitem = open(file, 'r')
        readitem = openitem.read()
        # print(openitem.read())

        matches = re.findall(r'\d{1}', readitem)
        print(matches)
        openitem.close()


read = Readfile()

read.openfile()


