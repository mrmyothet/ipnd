list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist = mylist + [6,7]

def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

print("demostrating proc_1")
print(list1)
proc((list1))
print(list1)
print
print("demostrating proc_2")
print(list2)
proc2((list2))
print(list2)

def proc3(mylist):
    mylist += [6,7]

list3 = [1,2,3,4,5]
print("demostrating proc_3")
print(list3)
proc3((list3))
print(list3)
