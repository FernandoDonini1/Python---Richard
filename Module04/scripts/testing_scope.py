# Demonstring variables scope

from click import clear

#Defining a function
def calculation():
    a = 5
    b = a + c
    c = 30
    return b

#Main program
clear()
print(calculation())