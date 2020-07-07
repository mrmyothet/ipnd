from stack import Stack
def divideBy16(decnum):
    remstack = Stack()
    while decnum > 0:
        rem = decnum % 16
        remstack.push(rem)
        decnum = decnum // 16
        binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())
    return binString
print(divideBy16(668))
