#Main program

import functions
from click import clear #Importing only clear function
clear() #Clear terminal
functions.brain()
print(functions.factorial_rec(5))
                