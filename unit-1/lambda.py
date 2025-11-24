#Using map function with lambda
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)
# Output: [1, 4, 9, 16, 25]



#Using filter function with lambda
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
# Output: [2, 4, 6]

names = ["Shridhar", "Sam", "Anya", "Sonia"]
long_names = list(filter(lambda n: len(n) > 4, names))
print(long_names)
# Output: ['Shridhar', 'Anya', 'Sonia']



#Using reduce function with lambda
from functools import reduce

nums = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)
# Output: 15


from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)
# Output: 24
