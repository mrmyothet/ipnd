def is_friend(name):
    if name[0] == "D":
        return True
    else:
        return False
print (is_friend("Diane"))
print (is_friend("Khun"))

# more simpler things
def is_friend(name):
    return name[0] == "D"
print (is_friend("Diane"))
print (is_friend("Khun"))
