# simple Sequential Searching
#k = [1,2,51,34,37,78]
#s = 37
#for i in k:
#    if i == s :
#        print("found")
#        break

# Sequential Searching with built in function(enumerate)
#k = [1,2,51,34,37,78]
#s = 37
#for (index,value) in enumerate(k):
#    if value == s:
#        print("found at",index)
#        break

# Sequential Searching with function
def search(array,search_value):
    for (index,value) in enumerate(array):
        if value == search_value:
            return index
    return -1
res = search([1,2,51,34,37,78],51)
if res != -1:
    print("Found at ",res)
else:
    print("Not found")
