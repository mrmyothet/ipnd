dict = {'Name': 'Aung Ko', 'Age': 7}
print("Name:" + dict["Name"])
print("Age: " + str(dict["Age"]))
print('++++++')

person1 = {'Name': 'Aung Ko', 'Age': 7}
person2 = {"Name": 'Ko Ko', 'Age': 8}
room = [person1,person2]
for person in room:
    print ("Name : "  + person["Name"])
    print("Age : "  + str(person['Age']))
print('========')
