def triangle_star(row):
        for x in range(1, row+1):
            for k in range(x):
                print("*", end="")
            print("")
x = input("How may rows : ")
try:
        x = int(x)
        triangle_star(x)
except ValueError:
        print("Please enter number only")


def triangle_star(row):
    for x in range(1,row+1):
        for k in range(x):
            print("*", end="")
print("")
x = input("How many rows : ")
try :
        x = int(x)
        triangle_star(x)
except ValueError:
    print("Please enter number only")


def triangle_star(row):
    for x in range(1,row+1):
        for k in range(x):
            print("*", end="")
            print("")
x = input("How many rows : ")
try :
        x = int(x)
        triangle_star(x)
except ValueError:
    print("Please enter number only")
