import math

# Describe the difference between a chained conditional and a nested conditional. Give your own example of each. 

# BOTH and AND or ARE SHORT-CIRCUIT OPERATORS IN PYTHON
# see https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

# chained conditions are EASIER TO READ because there is no nesting
def compare(x, y, z):
    if x > y and y < z:
        print('y is smallest')
    elif x > y > z:
        print('z is smallest')
    elif x < y < z:
        print('x is smallest')
    elif x == y or y == z:
        print('y is equal to x or z')
    else:
        print('x is equal to z')

compare(1,1,2)  # prints 'y is equal to x or z'
compare(1,2,3)  # prints 'x is smallest'
compare(1,2,1)  # prints 'x is equal to z'

# nested conditions are EASIER TO READ IF there would be 3 or more repetition of one of the conditions
# if conditions below would be chained (if not nested) it would be difficult to read

def compare_by_nesting(car_price, credit_score):
    if car_price > 30000:
        if credit_score > 780:
            print ('car loan approved')
        elif credit_score > 760:
            print ('20% prepayment required')
        elif credit_score > 740:
            print ('40% prepayment required')
        else:
            print ('sorry, your credit score is too low')
    elif car_price > 0:     # this condition would be reached only if first condition is false, hence 0 < car_price < 30000
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
                pass  # TODO: complete the conditions definition
# AND SO ON - using nesting it would be quite a long conditions list

find_minimum_using_conditions(5,4,3,2,1)    # prints '1 is minimum'
find_minimum_using_conditions(8,5,2,1,4)    # prints '1 is minimum'
find_minimum_using_conditions(8,5,2,0,1)    # prints '0 is minimum'

# There are many strategy options we can select from. One is chaining.
# Another option is using recursion to solve this with just one condition to check for minimum
def find_minimum_using_conditions_with_recursion(_array, index, _min):
    if index == 5:
        print(_min, ' is the minimum')
        return
    if _array[index] < _min:
        _min = _array[index]
    find_minimum_using_conditions_with_recursion(_array, index + 1, _min)

find_minimum_using_conditions_with_recursion([5,4,3,2,1], 0, math.inf)       # prints '1  is the minimum'
find_minimum_using_conditions_with_recursion([8,5,2,1,4], 0, math.inf)       # prints '1  is the minimum'
find_minimum_using_conditions_with_recursion([8,5,2,0,1], 0, math.inf)       # prints '0  is the minimum'
find_minimum_using_conditions_with_recursion([8,5,-2,0,1], 0, math.inf)      # prints '-2  is the minimum'
find_minimum_using_conditions_with_recursion([8,-5,2,0,1], 0, math.inf)      # prints '-5  is the minimum'

