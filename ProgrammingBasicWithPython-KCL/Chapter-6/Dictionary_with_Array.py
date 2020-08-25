person1 = {"Name":"Aung Ko","Age":7}
person2 = {"Name":"Ko Ko","Age":8}
room = [person1,person2]
for person in room:
    print("NAME:" + person["Name"])
    print("Age:" + str(person["Age"]))
