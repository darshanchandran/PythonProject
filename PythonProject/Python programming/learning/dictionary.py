#This program shows how dictonary could be used
import sys
states =  {
    'Karnataka' : 'KA',
    'TamilNadu' : 'TN',
    'AndraPradesh' : 'AP',
    'Kerala' : 'KL'
}

cities = {
    'TN' : 'Ooty',
    'KA' : 'Mysore',
    'AP' : 'Hyderabad',
    'KL' : 'Munnar'
}

print(states['Karnataka'])

if states['TamilNadu'] == 'TN':
    print("State Exists")
else:
    print("State does not Exists")

#Print all the States
print (states.items())

#Print all States method 2

for states,short in list(states.items()):
    print(f"{states} is Abbrev as {short}")

#Print cities in state lists

for states1,short1 in list(states.items()):
    print ("Hello")
