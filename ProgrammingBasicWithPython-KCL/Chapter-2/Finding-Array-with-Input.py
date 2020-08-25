list = [3,4,1,2,9,7]
userinput = input("Enter number to search in array : ")
try :
    userinput = int(userinput)
    found = False
    for (i,item) in enumerate(list):
        if item == userinput:
            found = True
            print("Your number can found in array.")
            print("Room : ",i)
            break;
    if found == False:
        print("Your Number cannot found in array!")
except ValueError:
    print("Please enter number only")
