from stack import Stack
def divideBy8(decNum):
    remstack = Stack()
    while decNum > 0:
        rem = decNum % 16
        remstack.push(rem)
        decNum = decNum // 16
        binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())
    return binString
print(divideBy8(668))
