from stack import Stack
def divideBy8(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 8
        remstack.push(rem)
        decNumber = decNumber // 8
        binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())
    return binString
print(divideBy8(668))

print("")

from stack import Stack
def divideBy16(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 16
        remstack.push(rem)
        decNumber = decNumber // 16
        binString = ""
    while not remstack.is_empty():
            binString = binString + str(remstack.pop())
    return binString
print(divideBy16(668))
