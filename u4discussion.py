
# 1. Wrong arguments were provided - precondition (condition that should have been met BEFORE function runs) is NOT met

def get_length(text):
    print (len(text))

# get_length(5)

# it prints
# Traceback (most recent call last):
#   File "...", line 15, in <module>
#     get_length(5)
#   File "...", line 13, in get_length
#     print (len(text))
# TypeError: object of type 'int' has no len()

# 2. Function was coded incorrectly - postcondition (condition that should have been # met AFTER function starts to run) is NOT met

def convert_to_text(val):
    if isinstance(val, str):
        return val
    if isinstance(val, int):
        return str ( val )

print (convert_to_text(5.5))

# prints None
# only two possible cases are covered here. Second condition should be
# if not isinstance(val, str):

# 3. Something wrong with ReturnED value or how it is used (e.g. it may not have been used)

# in this case because nothing is printed it looks like the function does not work. Actually, returned value is never used.
y = 5
x = convert_to_text(y)
if x == y:
    print (x)
    