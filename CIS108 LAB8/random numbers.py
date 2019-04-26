import random

def Comparenumbers(randNumber, userNumber):
    return userNumber - randNumber

def GetrandomNumber ():
    return random.randint (1,101)

# step 1 - get random nymber
randNumber = GetrandomNumber ()

keepGoing = True
while(keepGoing):

#step 2 ask user for input
    userNumber = input(" please choose a number between 1 and 100 : ")

#step 2.5 change to integer
    try:
        intUserNumber = int(userNumber)
    except:
        print("please try again with a number.")
        continue

# step 3 - compare numbers
    diffrence = Comparenumbers(randNumber , intUserNumber)


# step 4 - give user feedback
    if diffrence < 0:
        print ("your choice is too low.")
    elif diffrence > 0:
        print("your choice is too high.")
    else :
        print ("your choice is right.")
        keepGoing = False

print("game over!")