class Dog:
    def walk(self):
        print("I have 4 legs to walk")
        
class Emu:
    def walk(self):
        print("I have 2 legs to walk")
        
class Parrot:
    def fly(self):
        print("I can fly")
        
Dog().walk()
# walk(Dog())
Parrot().fly()
Emu().walk()
# walk(Emu())


#create a base class shape with a method area. derive classes circle and rectangle that override area using the relavant formula. call area for different object.