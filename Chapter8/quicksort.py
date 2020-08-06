def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
    return less + pivotList + more
qs = [4,7,8,1,6,3,2]
print(quickSort(qs))
print("")

from random import randint
def quickSort(array):
    if len(array) <= 1:
        return array
        room = randint(0,len(array) - 1)
        pivot = array[room]
        left = 0
        right = len(array) - 1
        while left <= right:
            while left < len(array) and array[left] < pivot:
                left += 1
            while right >= 0 and array[right] > pivot:
                right -= 1
                if left < right:
                    temp = array[left]
                    array[left] = array[right]
                    array[right] = temp
                    left += 1
                    right -= 1
                elif left == right:
                    left += 1
                    leftSort = quickSort(array[0:right+1])
                    rightSort = quickSort(array[left:len(array)])
                    return leftSort+rightSort
array = [4,2,3,1,6,8,7]
print(quickSort(array))
