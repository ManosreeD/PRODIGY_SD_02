#compare the numbers
import random

comp_choice=random.randint(0,9)
count=0
while True:
        count+=1
        
        user_choice=int(input("Enter the number:"))
        if(user_choice>comp_choice):
            print("It is too high")
        elif(user_choice<comp_choice):
            print("It is too low")
        elif(user_choice==comp_choice):
            print("Equal")
            print("umber of attempts:",count)
            break
        else:
            print("Invalid")

        
    






