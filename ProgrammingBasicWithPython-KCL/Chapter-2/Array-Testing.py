t = (6,7,8)
for i in range(len(t)):
    print(t[i])



list = [100,200,300,400]
x = 0
for i in range(len(list)):
    x = x + list[i]
    print("Total : ",x)



list = [100,200,300,400]
x = 0
for i in list:
    x = x + i
    print("Total --> ",x)




list = [100,200,300,400]
for (i,item) in enumerate(list):
    print("Index : ",i,"And Value : ",item)
