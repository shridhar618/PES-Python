class Laptop:
    #init method called automatically when the object has been created for this class
    #self represents the object
    def __init__(self, brand, model, price=25000):          #price is considered as a default argument
        '''self.brand associates the current object's brand attribute with the brand parameter'''
        self.brand=brand
        self.model=model
        self.price=price
    
    def turn_on(self):
        return f"{self.brand} {self.model} is now ON"
    
    def specifications(self):
        print(f"Laptop Details \n Brand: {self.brand} \n Model: {self.model} \n Price: ${self.price}")
        
        
    def turn_off(self):
        return f"{self.brand} {self.model} is now OFF"
    
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
