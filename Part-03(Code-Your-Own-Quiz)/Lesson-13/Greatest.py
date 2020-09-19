def greatest(list_of_Numbers):
    big = 0#
    for i in list_of_Numbers:
        if i > big:
            big = i
    return big
print(greatest([56,70,100]))
print(greatest([-9,4,8]))
