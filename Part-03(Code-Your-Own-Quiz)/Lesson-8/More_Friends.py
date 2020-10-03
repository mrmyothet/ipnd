def is_friend(name):
    return name[0] == "D" or name[0] == "N" #(Using (OR) operator)
print (is_friend("Do"))
print (is_friend("Nana"))
print (is_friend("Cho"))

def is_friend(name):
    if name[0] == "D":
        return True
    else:
          if name[0] == "N":
              return True
    return False
print (is_friend("Do"))
print (is_friend("Lwin"))
print (is_friend("Net"))
