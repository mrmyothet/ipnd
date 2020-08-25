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
