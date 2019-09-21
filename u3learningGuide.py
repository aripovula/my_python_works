import math

# PART 1
# Call your print_volume function three times with different values for radius.

def print_volume(r):
    volume = 4 / 3 * math.pi * r ** 3
    print(volume)

print_volume(30)    # prints    113097.33552923254

print_volume(90)    # prints    3053628.0592892785

print_volume(120)   # prints    7238229.473870883


# PART 2
# Write your own function that illustrates a feature that you learned in this unit.

# These functions perform pseudo-task of calculating log of product of 2 numbers and square root of third number

def get_product(param1, param2):     # params correspond to a and b in get_log10, but they do not have to be called a and b
    return param1 * param2

def get_sqrt(param):    # param corresponds to c in get_log10, but it does not have to be called c
    return math.sqrt(param)

def get_log10(a, b, c):
    the_product = get_product(a, b)
    the_sqrt = get_sqrt(c)
    print ("Is product equal to sq. roots ?  ", the_product == the_sqrt) # prints "Is product equal to sq. roots ?   True"
    return math.log10(the_product * the_sqrt)

x = 20
y = 5
z = 10000
print('Log10 of ', x, ' * ', y, ' * sq.root(', z, ') is ', get_log10(x, y, z)) # prints "Log10 of  20  *  5  * sq.root( 10000 ) is  4.0"
