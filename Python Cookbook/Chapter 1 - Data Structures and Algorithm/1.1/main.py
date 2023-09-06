# 1.1 - Unpacking a Sequence into Separate Variables

'''
Problem :
You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
Solution :
Any sequence (or iterable) can be unpacked into variables using a simple assignment
operation. The only requirement is that the number of variables and structure match
the sequence
'''
tuple = (5,4)
x,y = tuple
print(x)
print(y)

new_list = ['Hi',50,90,(2023,2013,2003)]
sal,num1,num2,year = new_list
print(sal)
print(num1,num2)
print(year)

# Even if the data structures are nested you can follow the same structure for the variables
hello,num3,num4,(year1,year2,year3) = new_list
print(year1,year2,year3)

# If there is a mismatch in the number of elements, you’ll get an error
'''
>>> p = (4, 5)
>>> x, y, z = p
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack
>>>
'''

