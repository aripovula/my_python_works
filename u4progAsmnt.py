
def testA(price, button):
    dis = 'discount is - '
    return f"{dis} {price - button} dollars"

print (testA(14, 4))

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_power(a, b):
    if a == b:    # base case # 1
        return True    # any number to power of 1 is the same value
    elif a == 1 and b == 1:   # base case # 2
        return True    # only positive integer that is a power of "1" is "1" itself
    elif a != 1 and b == 1:   # base case # 2
        return False 
    elif is_divisible(a, b):
        if a == b:
            return True
        elif a < b:
            return False
        else:
            # Recursive call
            return is_power(a/b, b)
    else:
        return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
