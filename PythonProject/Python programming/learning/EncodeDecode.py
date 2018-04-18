# Encode and Decode the hexa-decimal and utf-8 codes
import sys

decoding = input ("Enter the decoding unicode : ")
inputfile = input("Enter the hexa decimal file to be decoded : ")

def main(inputfilem,decodingm):
    line = inputfilem.readline()
    linestrip=line.strip()
    print(linestrip)
    dataencoded = linestrip.encode(decodingm)

    print(dataencoded.decode(hex))

inputfileo = open(inputfile)
main(inputfileo,decoding)
