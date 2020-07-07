#def bubble_sort(array):
#    for num in range(len(array) - 1,0,-1):
#        for i in range(num):
#            if array[i] > array[i + 1]:
#                temp = array[i]
#                array[i] = array[i + 1]
#                array[i + 1] = temp
#                return array
#alist = [1,6,4,7,8,9]
#print(bubble_sort(alist))

# Add exchange(variable) to control loop
def bubble_sort(array):
    exchange = True
    num = len(array) - 1
    while num > 0 and exchange:
        exchange = False
        for i in range(num):
            if array[i] > array[i + 1]:
                exchange = True
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                num = num - 1
    return array
alist = [1,6,3,4,8,9]
print(bubble_sort(alist))
