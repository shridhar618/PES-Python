class Laptop:
    #init method called automatically when the object has been created for this class
    #self represents the object
    def __init__(self, brand, model, price=25000):          #price is considered as a default argument
        '''self.brand associates the current object's brand attribute with the brand parameter'''
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level=100
        #every time an object iscreated for laptop, it has a battery level of 100 initialised
    
    def turn_on(self):
        return f"{self.brand} {self.model} is now ON"
    
    def specifications(self):
        print(f"Laptop Details \n Brand: {self.brand} \n Model: {self.model} \n Price: ${self.price}")
        
    def turn_off(self):
        return f"{self.brand} {self.model} is now OFF"
    
    def check_battery(self):
        return f'this laptop has {self.battery_level}% battery remaining'
    
    def update_battery_status(self, val):
        if 0<=val<=100:
            self.battery_level=val
            print(f"battery level of {self.brand}, {self.model} is updated to {self.battery_level}")
        else:
            print("Invalid battery level!!! please enter value between 0 and 100")
            
    def decrease_battery(self,usage):
        if usage<0:
            print('Usage amount cannot negative')
        elif self.battery_level-usage<=0:
            print("battery level is too low")
        else:
            self.battery_level=self.battery_level-usage
            print(f"battery level decreased by {usage}%/ current level: {self.battery_level}%")
            
    
print(type(Laptop))
print(id(Laptop))

l1=Laptop('Dell', 'Inspiron', 60000)
l2=Laptop('Apple', 'Macbook Air', 120000)

print(type(l1),id(l1),type(l2),id(l2))

l3=Laptop(25000, 'Pavilion', 'HP')
l4=Laptop(price=45000, model='ThinkPad', brand='Lenovo')
print(l3.brand,l3.model,l3.price)
print(l4.brand,l4.model,l4.price)

l5=Laptop('Asus', 'VivoBook')
print(l5.brand,l5.model,l5.price)

#Accesisng methods through objects
print(l1.turn_on())
l1.specifications()
print(l1.turn_off())

l8=Laptop('Dell','Inspiron 17', 89000)
print(l8.turn_on())

#every mrthod define in the class should take self as a parameter if the object needs to call the method
l1=Laptop('Dell','inspiron 15', 60000)
print(l1.brand,l1.model,l1.price,l1.battery_level)

print(l1.check_battery())


#change the value directly using the object
l1.battery_level=90
print(l1.check_battery())

#use a method that sets a new value each time the method is called.
l1.update_battery_status(80)
print(l1.check_battery())


l1=Laptop('apple', 'macbook', 60000)
l1.turn_on
l1.check_battery
l1.decrease_battery(20)
l1.check_battery

l1.update_battery_status(100)
l1.check_battery


#A dog has a name and is of a perticular breed and has an age. the dog barks and sleeps.
class Dog:
    def __init__(self,name,breed,age):
        self.name= name
        self.breed=breed
        self.age=age
        
    def barks(self):
        return f"the {self.name}, {self.breed}, {self.age} is barks"
    
    def sleeps(self):
        return f"the name:{self.name}, breed:{self.breed}, age:{self.age} sleeps"
        
d=Dog('Dogesh','Bully','5')
print(d.barks())
print(d.sleeps())

#A car has make model and year. a car can be started and can be stopped. every car has an initial reading of 0.
class Car:
    def __init__(self, model, year):
        self.model=model
        self.year=year
        self.initial_read=0
    
        
    def start(self, initial_reading=80):
        return f'the car {self.model} is started. the initial reading is {initial_reading}'

    
    def stop(self):
        return f"The car {self.model} is stopped. the initial reading is {self.initial_read}"
    
c=Car('Rolls Royce', 'Phantom')
print(c.start())
print(c.stop())




        