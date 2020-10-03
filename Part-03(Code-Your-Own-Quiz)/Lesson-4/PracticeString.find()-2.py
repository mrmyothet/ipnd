# Example 1: using find to print the second occurrence of a sub-string .
print("test".find("t"))
print("test".find("t,1"))

# Example 2: using a variable to store first location.
first_location = "test".find("t")
print("test".find("t",first_location + 1))

# Example 3: using find to get rid of exclamation mark!!.
example = "Wow! Python is great! Don't you think?"
first = example.find("!")
second = example.find("!", first + 1)
new_string = example[:first] + example[first + 1:second] + example[second+1:]
print(new_string)
new_string = example[:first] + "." + example[first + 1: second] + "." + example[second+1:]
print(new_string)
