from replit import clear
from art import logo

# Calculator
# add
def add(n1,n2):
  return n1+n2
# subtract
def subtract(n1,n2):
  return n1-n2
# multiply
def multiply(n1,n2):
  return n1*n2
# division
def division(n1,n2):
  return round(n1/n2)

operation={
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':division
  
}
def calculator():
    print(logo)
    num1=float(input("Enter your first number: "))
    for operator in operation:
      print(operator)
    operator=input("Pick an operation: ")
    num2=float(input("Enter your second number: "))
    calculation_function=operation[operator]
    first_answer=calculation_function(num1,num2)
    print(f"{num1} {operator} {num2}={first_answer}")
    
    
    should_continue=True
    while should_continue:
      resume=input(f"type 'y' to continue with calculating with {first_answer} or type 'n' to exit:")
      print(resume)
      if resume=='y':
        next_number=float(input("Enter your Next number: "))
        operator=input("Pick an operation: ")
        calculation_function=operation[operator]
        second_answer=calculation_function(first_answer,next_number)
        print(f"{first_answer} {operator} {next_number}={second_answer}")
        first_answer=second_answer
      else:
        should_continue=False
        clear()
        calculator()

calculator()
    
  
  