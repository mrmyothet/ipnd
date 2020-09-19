import random

random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0
count = 0

while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
  index = index + 1
print("0 --> ", count_list[0])
print("1 --> ", count_list[1])
print("2 --> ", count_list[2])
print("3 --> ", count_list[3])
print("4 --> ", count_list[4])
print("5 --> ", count_list[5])
print("6 --> ", count_list[6])
print("7 --> ", count_list[7])
print("8 --> ", count_list[8])
print("9 --> ", count_list[9])
print("10 --> ", count_list[10])
