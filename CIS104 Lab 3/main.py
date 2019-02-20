import calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
oper = (input ("enter an operation: "))

print = ("select an operation")

print = ("+ Add")

print = ("- Subtract")

print = ("* Multiply")

print = ("/ Divide")

print = ("^ Power")

print = ("I/i Invert")

print = ("S/s Store memory")

print = ("R/r Recall memory")

print = ("M/m Clear memory")

print = ("C/c Clear calculator")

print = ("X/x Exit =")

if oper == "+":
    
    answer = calculator.add (num1,num2)

    num1 = answer

    print (answer)

  

  elif oper == "-":

    answer = calculator.subtract (num1,num2)

    num1 = answer

    print (answer)

  

  elif oper == "*":

    answer = calculator.multiply (num1,num2)  

    num1 = answer

    print (answer)



  elif oper == "/":

    answer = calculator.divide (num1,num2)

    num1 = answer

    print (answer)



  elif oper == "^":

    answer = calculator.pow(num1,num2)

    num1 = answer

    print (answer)



  elif oper == "i" or "I":

    answer = calculator.invert(num1) 

    num1 = answer

    print (answer)

  

  elif oper == "c" or "C":

    answer = calculator.memClear(num1) 

    num1 = answer

    print ("Memory cleared.")

  

  elif oper == "s" or "S":

    answer = calculator.save(num1) 

    num1 = answer

    print (answer)



  elif oper == "r" or "R":

    answer = calculator.recall(num1) 

    num1 = answer

    print (answer)



  else:

    print("Invalid input.")          

  entry = input("> ") 

  num2 = float(input("Enter second number: "))   

  if entry != "x" or "X":

      continue