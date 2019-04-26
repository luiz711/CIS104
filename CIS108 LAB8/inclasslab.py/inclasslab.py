import random

def GetRandomNumber():
    return random.randint(1, 7)

keepGoing=True
while(keepGoing): 

    #randomly choose a number

    randNumber = GetRandomNumber()

    #print random number
    print(randNumber)

    #ask user if they want to roll again
    answer = input("would you like to roll again? Yes or no")

    #if so,
    if(answer.upper() =="YES" or answer.upper() == "Y"):
        #repeat
        print("ok we'll roll again.")
    #keepgoing = true
    #if not,
    else:
    #exit
        print("goodbye.")
        keepGoing=False
