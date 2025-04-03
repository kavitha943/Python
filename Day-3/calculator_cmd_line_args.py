#sys (system module) is available with python installation and inorder to use it just import the sys into
#the program to work with it.
# sys : reads the command line args as input 
import sys 

def add(num1, num2):
    result = num1 + num2
    return result
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2

#num1 = sys.argv[1] # default sys.argv reads inputs as a string 
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1,num2)
    print(output)
if operation == "sub":
    output = sub(num1,num2)
    print(output)
if operation == "mul":
    output = mul(num1,num2)
    print(output)
