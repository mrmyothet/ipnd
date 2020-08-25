#for x in range(0,5):
    #print("Hello World",x)


#def recursive(string, num):
#    if num == 5:
#        return
#    print(string,num)
#recursive(string,num+1)
#recursive("Hello World",0)

#def listsum(numList):
#    sum = 0
#    for i in numList:
#        sum = sum + i
#    return sum
#print(listsum([1,2,5,9,7]))

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
print(listsum([1,2,5,9,7]))
