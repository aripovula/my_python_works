# Learning Journal
# Part 1

import math

# Stage 1: defines raw function and checks if it returns value
def hypotenuse0(a, b):
    return 0

print(hypotenuse0(3, 4))    # prints 0

# Stage 2: checking if it takes arguments and makes correct calculations
def hypotenuse1(a, b):
    squared = a ** 2 + b ** 2
    c = math.sqrt( squared )
    print('c - ', c)
    return 0

hypotenuse1(3, 4)           # prints c - 5.0

# Stage 3: returns calculated value with 2 decimal points
def hypotenuse2(a, b):
    squared = a ** 2 + b ** 2
    c = math.sqrt( squared )
    return '{0:.2f}'.format(c)

print(hypotenuse2(3, 4))    # prints 5
print(hypotenuse2(2, 5))    # prints 5.39
print(hypotenuse2(4, 6))    # prints 7.21

# Part 2. Invent your own function that does some useful computation

# Stage 1: defines raw function and checks if it returns value
def get_rectangle_area0(a, b):
    return 0

print(get_rectangle_area0(3, 4))    # prints 0

# Stage 2: checking if it takes arguments and makes correct calculations
def get_rectangle_area1(a, b):
    area = a * b
    print('area - ', area)
    return 0

get_rectangle_area1(3, 4)           # prints area - 12

# Stage 3: returns calculated value
def get_rectangle_area2(a, b):
    area = a * b
    return area

print(get_rectangle_area2(3, 4))    # prints 12
print(get_rectangle_area2(2, 5))    # prints 10
print(get_rectangle_area2(4, 6))    # prints 24

# Part 3

# I feel good about the feedback and ratings I have received from my peers. They are objective and helpful. From some of them I learned new things.
# I do not know what my peers feel about the feedback and the ratings I gave them as we can not communicate with each other directly. I am doing my best to be objective and polite.

# Reference:  
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 