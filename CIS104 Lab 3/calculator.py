saved_mem = 0
short_term_mem = 0
long_term_mem = 0



def add(num1, num2):

    return num1 + num2



def  subtract(num1, num2):

    return num1 - num2



def multiply(num1, num2):

    return num1 * num2



def divide(num1, num2):

    return num1 / num2



def power(num1, num2):

    return num1 ** num2


#makes numbers negative
def invert(num1):

    return -num1


# saves answers
def  call_mem():

    return short_term_mem


#recalls memory
def save_mem(num1):

    global long_term_mem

    long_term_mem = num1


#clears memory
def clear_mem():

    global saved_mem

    saved_mem = 0