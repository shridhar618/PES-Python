def format_name(f_name, l_name ):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f" {formated_f_name} {formated_l_name}"

print(format_name("shridhar", "b"))



class Laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level=100
        
    def turn_on(self):
        print(f'{self.model} of {self.brand} is now turned on')
        
    def turn_off(self):
        print(f'{self.model} of {self.brand} is now turned off')
        
    def check_battery(self):
        print(f'the laptop has {self.battery_level}% battery life')
        
    def dec_battery(self, usage):
        if usage<0:
            print('usage amount cannot negative')
        elif self.battery_level-usage<0:
            print('battery level is too low. charge up now!')
        else:
            self.battery_level=usage
            print(f'battery decreased by {self.usage}% Current lkevel: {self.battery_level}')
    
            
            
            
class GamingLaptop(Laptop):
    #inherits the attributes from parent class laptop.
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)   