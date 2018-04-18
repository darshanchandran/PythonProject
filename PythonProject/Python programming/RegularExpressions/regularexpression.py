#This program shows how RE can be used with the re module

import re

sentence = "Vehicle number is KA439292"

#find all Strings with CAPS
stateregax = re.findall(r'[A-Z]',sentence)

# find all integers
numberregex = re.findall(r'\d{1,7}',sentence)

#find all integers and numericals
combineregex = re.findall(r'[A-Z]*\d{1,7}',sentence)
print(stateregax)
print(numberregex)

print(combineregex)
