x = False
while x == False:
    value = input("Enter the number between 0-9 : ")
    try :
        value = int(value)
        if value > 9:
            print("Your value is over 9")
        elif value < 0:
            print("Your value is less than 0")
        else:
            print("Your value is ",value)
            x = True
    except ValueError:
        print("Please enter number only")
