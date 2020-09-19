def product_list(list_of_Numbers):
    total = 1
    for i in list_of_Numbers:
        total = total * i
    return total
print(product_list([2,3]))
print(product_list([5,6]))
