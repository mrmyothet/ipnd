def max(lst):
    maxnumber = lst[0]
    for x in lst:
        if maxnumber < x :
            maxnumber = x
    return maxnumber
list1 = [1,2,3,5,4]
list2 = [100,200,900,400,500]
print("Maxnumber in list1 is ",max(list1))
print("Maxnumber in list2 is ",max(list2))
