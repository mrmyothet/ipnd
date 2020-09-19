# Example 1: Finding substring in a string
print("test".find("te"))
print("test".find("st"))
print("test"[2:])

# Example 2: Finding substring in a string which is stored as a variable.
my_string = "test"
print(my_string.find("te"))
print(my_string.find("st"))
print(my_string[2:])

# Example 3: Printing out everything after a certain substring.
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print(favorite_color)
print(favorite_color[7:])

# Example 4: Other interesting things about string.find().
print("text".find("text"))
print("text".find("Text"))
print("text".find(""))
print("text".find(" "))
