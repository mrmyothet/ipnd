x = input("Total number : ")
try :
    x = int(x)
    f = 0
    s = 1;
    for k in range(x):
        print(s,end=" ")
        t = s
        s = f + s
        f = t
    print("")
except ValueError:
    print("Please enter number only")
