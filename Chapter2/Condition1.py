firstnum = input("Enter First Number ? : ")
secondnum = input("Enter second Number (between 1-10) ? : ")
try :
    firstnum = int(firstnum)
    secondnum = int(secondnum)
    if secondnum  <= 0 :
        print ("Second number must be greater than 0")
    elif secondnum < 1 or secondnum > 10 :
        print ("Second number must be between 1-10")
    else:
        print (firstnum, "divided by ", secondnum)
        print (firstnum/secondnum)
except ValueError:
    print ("Please enter number only")
