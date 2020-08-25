### Looping QUESTION:
### Total Number
# Code: Q1
total = 0;
for x in range (10):
    total = total + x
print(total)
# Code: Q2
total = 0;
for x in range (10):
    total = total + 1
print(total)

### Fibonacci

x = input("Total number : ")
try:
    x = int(x)
    f = 0
    s = 1;
    for k in range(x):
        print (s, end= " ") # end is for ending with space and don't use another line
        t = s
        s = f + s
        f = t
        print ("") # just for line break in terminal
except ValueError:
    print("Please enter number only")

### Even/Odd

x = input ("Enter Number : ")
try :
    x = int(x)
    for k in range(1,x+1):
        if k % 2 == 0 :
            print(k , " Is Even")
        else:
            print(k, " Is Odd")
except ValueError:
        print("Please enter number only")

### Arry QUESTION:
### Min Number

list = [1048,1255,2125,1050,1001,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber > x :
        minnumber = x
print("Min number in array is ", minnumber)

### Search in array
list = [3,4,1,2,9,7]
x = input(" Enter your number to Search : ")
try :
    x = int(x)
    found = False
    for (i,item) in enumerate(list):
        if (item==x) :
            found = True
            print("Found at", i)
            break;
            if found == False:
                print ("not found in the list")
except ValueError:
    print("please enter number only")

# Finding Max number with room
list =[1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
room = 0;
for (i,item) in enumerate(list):
    if maxnumber < item :
        maxnumber = item
        room = i
print ("maxnumber in array is ", maxnumber, "Found at room", room)

# triangle_star QUESTION:

def triangle_star(R):
    for x in range(1,R+1):
        for k in range(x):
            print("*", end="")
        print("")
x = input("How many rows : ")
try :
    x = int(x)
    triangle_star(x)
except ValueError:
    print("Please enter number only")
