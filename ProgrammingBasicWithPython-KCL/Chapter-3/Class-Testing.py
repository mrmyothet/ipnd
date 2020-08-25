class animal:
    number_of_legs = 0
dog = animal()
dog.number_of_legs = 4
print("Dog has {} legs".format(dog.number_of_legs))
chicken = animal()
chicken.number_of_legs = 2
print("Chicken has " + str(chicken.number_of_legs) + " legs")
