def calculator():
    print("Simple Calculator")
    print("choose an operation: +,-,*,/")
    num1=float(input("Enter First number:"))
    operation=input("Enter operation(+,-,*,/):")
    num2=float(input("Enter Second number:"))
    if operation=='+':
        result=num1+num2
    elif operation=='-':
        result==num1-num2
    elif operation=='*':
        result==num1*num2
    elif operation=='/':
        if num2==0:
            print("Error:Division by zero is not allowed.")
            result=num1/num2
    else:
        print("Invalid operation!")
    print(f"Result:{num1}{operation}{num2}={result}")

calculator()
    