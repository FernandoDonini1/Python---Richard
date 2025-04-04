#Testing scope 2

from click import clear

def calculation():
    global c,d
    a = 5
    b = a + c
    c = 30
    d = 50
    return b

#Main program
c = 10
print(calculation())
print("C value=",c,"D value= ",d)
