x = input("Enter first value : ")
y = input("Enter second value : ")
op = input("Operator (+ - * / ) : ")
try :
    x = int(x)
    y = int(y)
    output = True
    if op == "+" :
        result = x + y
    elif op == "-" :
        result = x - y
    elif op == "*" :
        result = x * y
    elif op == "/" :
        result = x / y
    else:
        output = False
        print("Wrong Operator")
    if output :
            print("Result is" ,result)
except ValueError:
    print("Please enter number only")
    print(ValueError);
