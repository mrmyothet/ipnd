def printHello():
    print("Hello")
printHello()

def printHello(val):
    print ("Hello", val)
printHello("World")
printHello("Python")

def sum(val1,val2) :
    return val1 + val2
print ("Sum : ", sum(1,4))

list = [1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber < x :
        maxnumber = x
print("Max number in array is ", maxnumber)
print("")

list = [1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber < x :
        maxnumber = x
print ("Max number in array list is", maxnumber)
list2 = [1,2,5,6,9,3,2]
maxnumber = list2[0]
for x in list2:
    if maxnumber < x :
        maxnumber = x
print("Max number in array list2 is", maxnumber)

print("")

def max(lst):
    maxnumber = lst[0]
    for x in lst:
        if maxnumber < x :
            maxnumber = x
    return maxnumber
list = [1048,1255,2125,1050,2506,1236,2010,1055]
list2 = [1,2,5,6,9,3,2]
print("Max number in array list is ", max(list))
print("Max number in array list is ", max(list2))
