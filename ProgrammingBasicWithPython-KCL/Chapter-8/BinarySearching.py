# BinarySearching simple code
#k = [8,14,18,20,26,66,78]
#s = 18
#found = False
#first = 0
#last = len(k) - 1
#while first <= last and not found:
#    mid = (first + last)//2
#    mid_value = k[mid]
#    if mid_value == s:
#        found = True
#    else:
#        if s < mid_value:
#            last = mid - 1
#        else:
#            first = mid + 1
#            print(found)

 #BinarySearching with Function
#def binary_search(array,item):
#    first = 0
#    last = len(array) - 1
#    while first <= last:
#        mid = (first + last)//2
#        mid_value = array[mid]
#        if mid_value == item:
#            return ("found at",)
#        else:
#            if item < mid_value:
#                last = mid - 1
#            else:
#                first = mid + 1
#    return ("Not found")
#print(binary_search([8,14,18,20,26,66,78],18))
#print(binary_search([8,14,18,20,26,66,78],11))


#BinarySearching with Recursive
def binary_search(array,item):
    if len(array) == 0:
        return False
    mid = len(array) //2
    mid_value = array[mid]
    if mid_value == item:
        return True
    else:
        if item < mid_value:
            return binary_search(array[:mid],item)
        else:
            return binary_search(array[mid+1:],item)
print(binary_search([8,14,18,20,26,66,78],18))
print(binary_search([8,14,18,20,26,66,78],19))
