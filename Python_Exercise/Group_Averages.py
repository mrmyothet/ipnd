# There are a variable number of schools
# Each school has different number of students
# Find averages for each school
# Return school with highest average
# Minimal use of built-in functions
def get_average(a_list):
    total = 0
    for mark in a_list:
        total += mark
    average = total/len(a_list)
    return average
def get_max(a_list):
    max_value = 0
    for mark in a_list:
        if mark > max_value:
            max_value = mark
    return max_value

mark_list = [[89, 78, 56, 79, 86, 72, 91, 63, 53],
             [68, 72, 73, 89, 74, 78],
             [97, 58, 72, 68, 81, 67, 93],
             [45, 89, 98, 45, 67, 34, 89, 55],
             [34, 99, 98, 87, 76],
             [98, 56, 98, 78, 99, 78, 89, 99]
            ]

average_list = []
for group_list in mark_list:
    average_value = get_average(group_list)
    average_list.append(average_value)
max_average = get_max(average_list)
print("The highest average mark for the " + str(len(mark_list))  + \
      " schools is " + str(max_average))
print("School " + str(average_list.index(max_average)) + \
      " gives the highest average.")
