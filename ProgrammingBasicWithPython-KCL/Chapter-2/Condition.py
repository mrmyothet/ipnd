firstnum = input("Enter first number : ")
secondnum = input("Enter second number : ")
try :
    firstnum = int(firstnum)
    secondnum = int(secondnum)
    if secondnum <= 0:
        print("Second number must be greater than zero")
    elif secondnum < 1 or secondnum > 10:
        print("Second number must be between 0-10")
    else:
        print(firstnum,"divided by",secondnum)
        print(firstnum/secondnum)
except ValueError:
    print("Please Enter number only")
