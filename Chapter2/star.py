for x in range(4):
    print("*")

for x in range(4):
    for k in range(4):
        print("*", end ="")

for x in range(4):
    for k in range(4):
        print("*", end ="")
    print("")
print('--------')

for x in range (4):
    for k in range (x):
        print("*", end = "")
    print("")
print("-----------")
for x in range(1,6):
    for k in range(x):
        print("*" , end ="")
    print("")
print ("--------")

def triangle_star(row):
    for x in range(1, row+ 1):
        for k in range(x):
            print("*", end="")
        print("")
x = input("How many rows? : ")
try:
    x = int(x)
    triangle_star(x)
except ValueError:
    print("Please enter number only")
