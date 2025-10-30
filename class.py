class Laptop:
    #init method called automatically when the object has been created for this class
    #self represents the object
    def __init__(self, brand, model, price):
        '''self.brand associates the current object's brand attribute with the brand parameter'''
        self.brand=brand
        self.model=model
        self.price=price
    
    def turn_on(self):
        return f"{self.brand} {self.model} is now ON"
            