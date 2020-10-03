# This way is a little bit asymmetrical.
def bigger(a,b):
    if a > b:
        return a
    return b
print (bigger(4,5))
print (bigger(3,3))
print (bigger(6,9))

def bigger(a,b):
    if a > b:
        r = a
    else:
        r = b
    return r
print (bigger(5,9))

def bigger(a,b):
    return max(a,b)
print(bigger(43,91))
