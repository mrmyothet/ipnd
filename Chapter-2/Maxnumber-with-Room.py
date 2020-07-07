list = [50,100,300,200,250]
maxnumber = list[0]
room = 0;
for (i,item) in enumerate(list):
    if maxnumber < item :
        maxnumber = item
        room = i
print("Room is ",room)
print("Maxnumber is ",maxnumber)
