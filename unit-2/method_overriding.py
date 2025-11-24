class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):   # overriding parent method
        print("Dog barks 🐶")

class Cat(Animal):
    def sound(self):   # overriding parent method
        print("Cat meows 🐱")

# Create objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()


# ---------------------------Output:-----------------------------
# Animals make sounds
# Dog barks 🐶
# Cat meows 🐱
