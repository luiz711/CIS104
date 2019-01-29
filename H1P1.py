first_name = input('Enter your first name:')
last_name = input('Enter Your Last name:')
age = int(input('Enter Your Age:'))
confidence = float(input('What is Your Confidence in Programmers between 0-100%:'))
dog_age = (age * 7)
print ("Hello,",first_name,last_name,"nice to meet you!,""you might be",age,"in human years but in dog years you are,",dog_age)
if confidence < 50:
     print ("I agree programmers cant be trusted!")
else:
         print ("Writing good code take hard work")
    