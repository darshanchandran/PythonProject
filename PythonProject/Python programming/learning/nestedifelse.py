#This program shows how nested if else works

selection = input(" Welcome Soundarya : \n Enter 1 if you are feeling sad \n Enter 2 if you are happy \n Enter 3 if you feel loved : \n > ")

if selection == "1":
     reason = input (" Enter 1 if the reason is your husband : \n Enter 2 if the reason is someone else : \n > ")
     if reason == "1":
         print("Dont worry , your husband is there for you always. Stay happy")
     elif reason =="2":
         print("Dont worry , Ignore what ever people said and be happy with your husband")
     else:
         print("Nothing to worry , stay Happy")
elif selection == "2":
    print("That's wonderful !! Stay happy and your husband like it")
else:
    print("Wow , your husband loves you too!")
