for x in range(0, 5):
    print("Hello World", x)

print('+++++++++')

# Looping with recursive

def recursive(string, num):
    if num == 5:
       return
    recursive("Hello World", 0)
    print (string,num)
    recursive(string,num+1)

#### Calculating the Sum of a list of numbeers

def listsum(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    return sum
print("Sum :",listsum([1,2,5,9,7]))

k = [1,2,5,9,7]
print(k[1:])
print(k[2:4])
print(k[:3])

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
print(listsum([1,2,5,9,7]))
