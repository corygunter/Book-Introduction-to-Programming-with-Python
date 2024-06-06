# Basic Operations Exercises

first_name = 'Cory'
last_name = 'Gunter'

print('Cory ' + 'Gunter')
print('Cory' + ' ' + 'Gunter')
print(f'{first_name} {last_name}')

# 4936

number = 4936

ones = (4936 % 10)
tens = (number // 10)
hundreds = (tens // 10)
thousands = (hundreds // 10)

print(ones)
print(tens % 10)
print(hundreds % 10)
print(thousands % 10)

# What does the following code do? Why?
# print('5' + '10')

# It prints 510 through concatenation because '5' and '10' are strings not integers or floats.

# Refactor the code to print 15
print(int('5') + int('10'))

# Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:
# foo = ['a', 'b', 'c']
# print(foo[3])      
# will this result in an   error?

# Yes, [3] would be trying to access the 4th value in the list.

# To what value does the following expression evaluate?

# 'foo' == 'Foo'

# It is checking to see if 'foo' is equal to Foo' which will evaulate as False because of casing.

# What will the following code do? Why? 
# int('3.1415')

# It will waise a ValueError bcause 3.1415 isn't a valid integer.

# To what value does the following expression evaluate?
# '12' < '9'

# It will return true because it's checking the values of the first unit of the string and 9 > 1
# It preforms character-by-character comparison going left to right.


