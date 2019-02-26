import calculator
#functions for user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
oper = (input ("enter an operation: "))
#diffrent options they can choose to do in the calculator
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

if oper == "+": #type of function being used

    answer = calculator.add (num1,num2) #calling the numbers being used in the function they picked

    num1 = answer #outputs answer

    return (answer)

  

 elif oper == "-":

    answer = calculator.subtract (num1,num2)

    num1 = answer

    return (answer)

  

  elif oper == "*":

    answer = calculator.multiply (num1,num2)  

    num1 = answer

    return (answer)



  elif oper == "/":

    answer = calculator.divide (num1,num2)

    num1 = answer

    return (answer)



  elif oper == "^":

    answer = calculator.pow(num1,num2)

    num1 = answer

    return (answer)



  elif oper == "i" or "I":

    answer = calculator.invert(num1) 

    num1 = answer

    return (answer)

  

  elif oper == "c" or "C":

    answer = calculator.memClear(num1) 

    num1 = answer

    return ("Memory cleared.")

  

  elif oper == "s" or "S":

    answer = calculator.save(num1) 

    num1 = answer

    return (answer)



  elif oper == "r" or "R":

    answer = calculator.recall(num1) 

    num1 = answer

    return (answer)



  else:

    print("Invalid input.")          

  entry = input("> ") 

  num2 = float(input("Enter second number: "))   

  if entry != "x" or "X":

      continue