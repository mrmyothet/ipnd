list = [1,5,2,7,8,9,200,155]

print (list[0])
print(list[5])
print(list[7])


list = [1,5,2,7,8,9,200,155]
#Total room
print ("Total room in array is ", len(list))


list = [1,5,2,7,8,9,200,155]
for i in range(len(list)):
    print(list[i])

print("")

list = [1,5,2,7,8,9,200,155]
x = 0
for i in range(len(list)):
    x = x + list[i]
    print("Total:",x)

print("")

list = [1,5,2,7,8,9,200,155]
x = 0
for i in list:
    x = x + i
print("Total:",x)

print("")

list = [1,5,2,7,8,9,200,155]
for (i,item) in enumerate(list):
    print("Index:",i,"And Value:", item)

print ("")

 # Finding Max number
list = [1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber < x :
        maxnumber = x
print("MAX number in array is",maxnumber)
