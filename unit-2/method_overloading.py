#(1).   ---------------------Using Default Arguments---------------------#
class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Sum of three numbers:", a + b + c)
        elif a is not None and b is not None:
            print("Sum of two numbers:", a + b)
        else:
            print("Please provide at least two numbers")

# Create object
calc = Calculator()
calc.add(10, 20)        # 2 arguments
calc.add(10, 20, 30)    # 3 arguments
calc.add(10)            # 1 argument

#---------------------------output:-----------------------------
# Sum of two numbers: 30
# Sum of three numbers: 60
# Please provide at least two numbers


#--------------------------------------------------------------------------------------------------------------------------

#(2).   ---------------------Using *args---------------------#
class Display:
    def show(self, *args):
        for item in args:
            print(item, end=' ')
        print()

d = Display()
d.show(10)
d.show(10, 20)
d.show(10, 20, 30)

#---------------------------output:-----------------------------
# 10
# 10 20
# 10 20 30
