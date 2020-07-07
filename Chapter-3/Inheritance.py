class animal:
    number_of_legs = 0
    def sleep(slef):
        print("zzz")
    def count_legs(self):
        print("I have {} legs".format(self.number_of_legs))
class dog(animal):
    def bark(self):
        print("Woof")
mydog = dog()
mydog.number_of_legs = 4
mydog.bark();
mydog.sleep()
mydog.count_legs()
