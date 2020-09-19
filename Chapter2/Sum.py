x = input("Enter first value: ")
y = input("Enter second value: ")
print ("X + Y = ", x + y)


x = input("Enter first value: ")
y = input("Enter second value: ")
try:
    x = int(x)
    y = int(y)
    print("X + Y = ", x + y)
except ValueError:
    print ("Please enter number only")
