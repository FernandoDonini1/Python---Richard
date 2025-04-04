### File that will contain functions

def brain(title="Hello World", columns=60):
    spaces = (columns-len(title))//2
    text = " " * spaces + title + " " * spaces
    print(text)

def factorial(value):
    ret = 1
    for i in range(value,1,-1):
        ret *= i
    #return ret #Return the value 
    print("Factorial of",value,"=",ret)

#Using recursivity
def factorial_rec(value):
    if value == 1: return 1
    return value * factorial_rec(value-1)

if __name__ == "__main__": #Only executed when call the functions.py
    brain("Hello World")



