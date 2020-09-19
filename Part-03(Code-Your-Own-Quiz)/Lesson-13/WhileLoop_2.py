import random
random_list = []
list_length = 20
while len(random_list) < list_length:
    random_list.append(random.randint(0,10))
index = 0
count = 0
while index < len(random_list):
    if random_list[index] == 9:
        count = count + 1
    index = index + 1
print(random_list)
print(count)
