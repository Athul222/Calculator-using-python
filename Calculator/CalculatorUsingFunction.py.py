from replit import clear
from CalcLogo import logo

def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def mul(a , b):
    return a * b
def div(a , b):
    return a/b
def modu(a , b):
    return a % b

running = True

temp = {
    "+":add ,
    "-":sub , 
    "*":mul, 
    "/":div ,
    "%":modu}

def calculaton_func():
    print(logo) #when we clear the screen 
    num1 = float(input("Enter the first num: "))
    print("operations: ")
    for item in temp:
        print(item)
    running = True
    while running:
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the next num: "))
        calculations = temp[operator]
        answer = calculations(num1 , num2)
        print(f"{num1} {operator} {num2} = {answer}")
        choice = input(f"Do you want to claculate again. Type 'c' to do calculation from current value {answer}, 'n' to new calculations and 'e' for exit." ).lower()
        if choice == 'c':
            num1 = answer
        elif choice == 'n':
            clear()
            calculaton_func()
        else:
            running = False
            print("GoodBye!")
            break
        
calculaton_func()