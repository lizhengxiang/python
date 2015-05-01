import math as foobar
print foobar.sqrt(9)
from math import sqrt as Sqrt
print Sqrt(9)
#import stdin
age = 10
#assetr  age >= 0, 'The age must be realistic'

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt'] 
len(scope)
print scope.keys()

print eval('9+7*10')

def square(x):
	'Calculates the square of the number x'
	return x*x
a = square(3)
print a
print square.__doc__
#help(square)

def func(x):
	print x
x = func(3)
print x
print None == 0

storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['list'] = {}

me = 'lizhengxiang'
storage['first']['li'] = me
storage['middle']['zhneg'] = me
storage['list']['xiang']  = me

print storage['list']['xiang']
