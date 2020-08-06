x = False
while x == False :
        value = input("Enter the number between 0 and 9: ")
        try:
            value = int (value)
            if value > 9 :
                print ("Your value is over 9")
            elif value < 0:
                print ("Your value is less than 1")
            else:
                print ("Your number is ", value)
            x = True
        except ValueError:
            print ("Please enter the number between 0 and 9")
