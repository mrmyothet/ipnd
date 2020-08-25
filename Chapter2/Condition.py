firstnum = input("Enter First Number ? : ")
secondnum = input("Enter Second Number ? : ")
try :
    firstnum = int(firstnum)
    secondnum = int(secondnum)
    if secondnum <= 0 :
        print("Second number must be greater than 0")
    else:
        print (firstnum, "divided by ", secondnum)
        print (firstnum/secondnum)
except ValueError:
        print ("please enter number only")
