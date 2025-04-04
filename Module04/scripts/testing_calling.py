#Call with parameters test program

from click import clear

#Defining functions
def variable_calcule(a,b):
    ret = a + b
    a = 15
    b = 20
    return ret
def using_list(list):
    list.append(5)
    list.append(6)
    return len(list)

# Main program
d, e = 5, 6
list = [1,2]

#Using the functions
clear()
print(variable_calcule (d,e))
print(d,e)
print("Antes",list)
print(using_list(list))
print("Depois",list)
