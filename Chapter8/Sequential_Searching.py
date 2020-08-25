k = [1,2,51,34,37,78]
s = 34
for i in k:
    if i == s:
        print("found")
        break

# searching with enumerate:
k = [1,2,51,34,37,78]
s = 37
for (index,value) in enumerate(k):
    if  value == s:
        print("found at ", index)
        break

# function ဖြင့်သပ်ရပ်အောင်ရေးခြင်း
def search(array,search_value):
    for (index,value) in enumerate(array):
        if value == search_value :
            return index
    return -1
res = search([1,2,51,34,37,78],34)
if res != -1:
        print("Found at ",res)
else:
        print("Not Found")
