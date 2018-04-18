# This program plays with the lists
import sys
a = [22,33,55]
print(a[0])  #Note the square syntax

print(len(a))  # Check the length of the lists

b = 6

while len(a) <= 5:
    print("length of the list is : ",len(a))
    print(f"Appending {b} to the list")
    a.append(b)
    b += 1
print(len(a))

length = len(a)

print(a[0:length])
print(*a)
