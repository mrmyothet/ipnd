# For loop
def find_element(list,y):
    i = 0
    for item in list:
        if item == y:
            return i
        i = i + 1
    else:
        return -1
print(find_element([2,3,4],5))
print(find_element([12,13,14],12))
print(find_element([100,200,300],300))


# While loop
def find_element(list,y):
    i = 0
    while i < len(list):
        if list[i] == y:
            return i
        i = i + 1
    return -1
print(find_element([2,3,4],5))
print(find_element([12,13,14],12))
print(find_element([100,200,300],300))


# in operation
def find_element(list,y):
    if y in list:
        return list.index(y)
    else:
        return -1
print(find_element([1,2,3,4],4))
print(find_element([100,200,300,350,400],400))

# not in operation
def find_element(list,y):
    if y not in list:
        return -1
    return list.index(y)
print(find_element([1,2,3,4],4))
print(find_element(["Su Su","Ma Ma",400],"Ma Ma"))
