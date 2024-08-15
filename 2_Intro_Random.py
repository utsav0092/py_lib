from numpy import random

'''Provide the random integer value'''
a = random.randint(1, 100)
print(a)

'''Provide the random floating value'''
b = random.rand()
print(b)

'''Return 100 random floating values'''
c = random.rand(100)
print(c)

'''Return values between 100 with 2 rows and 5 columns'''
d = random.randint(100, size=(2, 5))
print(d)

'''Give random from the given list'''
e = random.choice([3, 4, 5, 10, 32], size=(4, 2))
print(e)
