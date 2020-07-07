dict = {"Name":"Aung Ko","Age":7}
dict["Age"] = 9
del dict["Name"]
print("NAME:" + dict["Name"]) # you will get error...
print("Age:" + str(dict["Age"]))
