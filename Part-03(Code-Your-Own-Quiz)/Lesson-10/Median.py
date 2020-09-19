def median(a,b,c):
    if a > b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c
print (median(2,3,4))
print (median(9,6,7))
print (median(7,8,9))  #This is my way.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def median(a,b,c):
    if bigger(a,b)<=c:
        return bigger(a,b)
    if bigger(a,c)<=b:
        return bigger(a,c)
    if bigger(c,b)<=a:
        return bigger(c,b)
print (median(5,9,7))  #The one way at Udacity.



def biggest(a,b,c):
    return bigger(c,bigger(a,b))
def median(a,b,c):
    big = biggest(a,b,c)
    if big == c:
        return bigger(a,b)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
print (median(5,9,7))  #The other way to solve this problem.
print (median(5,6,7))
