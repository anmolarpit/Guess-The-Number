import random

print("WELCOME TO ROCK|PAPER|SCISSORS")
a= int(input("Choose \n1.Rock \n2.Paper \n3.Scissors \nEnter:"))
if (a == 1):
    print("Your choice is Rock")
elif (a == 2):
    print("Your choice is Paper")
elif (a == 3):
    print("Your choice is Scissors")

print("Now the computer choice is..")
b= random.randint(1,3)

if (b == 1):
    print("Rock")
elif (b == 2):
    print("Paper")
elif (b == 3):
    print("Scissors")

if (a == 1 and b== 1):
    print("DRAW")
elif(a==1 and b == 2):print("LOST")
elif(a==1 and b==3):print("------WON------")

if (a == 2 and b== 2):
    print("DRAW")
elif(a ==2 and b == 3):print("LOST")
elif (a==2 and b==1):print("------WON------")

if (a == 3 and b== 3):
    print("DRAW")
elif(a ==3 and b == 1):print("LOST")
elif(a == 3 and b ==2):print("------WON------")

