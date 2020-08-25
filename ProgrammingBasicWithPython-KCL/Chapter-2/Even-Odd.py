userinput = input("Enter the number : ")
try :
    userinput = int(userinput)
    for input in range(1,userinput+1):
        if input % 2 == 0:
            print(input," is Even")
        else:
            print(input," is Odd")
except ValueError:
    print("Please enter number only")
