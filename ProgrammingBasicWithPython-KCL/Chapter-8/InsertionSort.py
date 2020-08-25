def insertionsort(array):
    for i in range(1,len(array)):
        element = array[i]
        j = i
        while j > 0 and array[j-1] > element:
            array[j]  = array[j-1]
            j = j - 1
            array[j] = element
    return array
print(insertionsort([5,6,4,7,12,9]))
