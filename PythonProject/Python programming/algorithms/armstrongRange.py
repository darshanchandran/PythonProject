#This program finds if a number is armstrong

def armstrong(num3):
    #num3 = input("Enter the number : ")
    num3 = int(num3)
    # Seperate the last integer
    num = num3

    # Multiply the seperated number three times

    sum = 0

    sum = int(sum)
    while num >= 1:
        num1 = int(num) % 10

        # Multiply the seperated number three times

        sum = sum + (num1 * num1 * num1)
        num = num / 10

    if num3 == sum :
        print(f"{num3} is an armstrong number")
    else :
        pass

# Define the range to find the armstrong number

range1 = input (" Enter the starting range : ")
range2 = input ("Enter the ending range number : ")

range1 = int(range1)
range2 = int(range2)
for i in range(range1,range2):
    armstrong(i)
