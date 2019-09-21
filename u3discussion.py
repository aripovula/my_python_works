import math

# Describe the difference between a chained conditional and a nested conditional. Give your own example of each. 

# BOTH and AND or ARE SHORT-CIRCUIT OPERATORS IN PYTHON
# see https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

# chained conditional - EASIER TO READ
def compare(x, y, z):
    if (x > y and z > y) or (x > z > y):
        print('y is smallest')
    elif x > y and z < y:
        print('z is smallest')
    elif x < y and z > y:
        print('x is smallest')
    else:
        print('at least 2 of 3 numbers are equal')

compare(1,1,2)  # prints 'at least 2 of 3 numbers are equal'
compare(1,2,3)  # prints 'x is smallest' and so on

# nested conditional - EASIER TO COVER IF MORE THAN 4 OR 5 COMBINATIONS
# if below example is defined with nesting it will also become harder to read

def compare_by_nesting(car_price, credit_score):
    if car_price > 30000:
        if credit_score > 780:
            print ('car loan approved')
        elif credit_score > 740:
            print ('40% prepayment required')
        else:
            print ('sorry, your credit score is too low')
    elif car_price > 0:
        if credit_score > 740:
            print ('car loan approved')
        elif credit_score > 720:
            print ('30% prepayment required')
        else:
            print ('sorry, your credit score is too low')
    else:
        print ('we should throw an exception here with text Negative Price Exception')


# Deeply nested conditionals can become difficult to read. Describe a strategy for avoiding nested conditionals. 
# Give your own example of a nested conditional that can be modified to become a single conditional, and 
# show the equivalent single conditional. 

# if nesting level is more than 2 or 3 it MAY become hard or time-consuming to read

def find_median_using_conditions(a, b, c, d, e):
    if a > b:
        if b > c:
            if c > d:
                if d > e:
                    print (c, 'is median')
                if d < e:
                    if e < c:
                        print (c, 'is median')
                    if e > c:
                        print (e, 'is median')
            if c < d:
                pass
# AND SO ON - using nesting it would be quite a long conditions list

find_median_using_conditions(5,4,3,2,1)    # prints '3 is median'
find_median_using_conditions(8,5,2,1,4)    # prints '4 is median'


def find_minimum_using_conditions(a, b, c, d, e):
    if a > b:
        if b > c:
            if c > d:
                if d > e:
                    print (e, 'is minimum')
                if d < e:
                    if e < c:
                        print (d, 'is minimum')
                    if e > c:
                        print (d, 'is minimum')
            if c < d:
                pass
# AND SO ON - using nesting it would be quite a long conditions list

find_minimum_using_conditions(5,4,3,2,1)
find_minimum_using_conditions(8,5,2,1,4)
find_minimum_using_conditions(8,5,2,0,1)

def find_minimum_using_conditions_with_recursion(_array, index, _min):
    if index == 5:
        print(_min)
        return
    # print(index, _min)
    if _array[index] < _min:
        _min = _array[index]
    find_minimum_using_conditions_with_recursion(_array, index + 1, _min)

find_minimum_using_conditions_with_recursion([5,4,3,2,1], 0, math.inf)
find_minimum_using_conditions_with_recursion([8,5,2,1,4], 0, math.inf)
find_minimum_using_conditions_with_recursion([8,5,2,0,1], 0, math.inf)
find_minimum_using_conditions_with_recursion([8,5,-2,0,1], 0, math.inf)
find_minimum_using_conditions_with_recursion([8,-5,2,0,1], 0, math.inf)
