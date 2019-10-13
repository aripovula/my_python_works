import math

def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

# Write a new recursive function countup that expects a negative argument and counts “up” from that 
# number. Output from running the function should look something like this:

# >>> countup(-3)
# -3
# -2
# -1
# Blastoff!

def count_up(n):
     if n >= 0:
          print('Blastoff!')
     else:
          print(n)
          count_up(n+1)

countdown(3)
count_up(-3)

# Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but 
# raw_input for Python 2.)
# If the number is positive, the program should call countdown. If the number is negative, the program should 
# call countup. Choose for yourself which function to call (countdown or countup) for input of zero.
# Provide the following.
# The code of your program.

start_point_str = input('Please type counter start point (must be integer) = ')
start_point = int(start_point_str) # ideally we should verify that it is indeed an integer using try: except
if start_point >= 0:    # if start_point == 0 call count_down
    countdown(start_point)
else:
    count_up(start_point)

# Output for the positive number:
# 3
# 2
# 1
# Blastoff!

# Output for the negative number:
# -3
# -2
# -1
# Blastoff!

# Output for zero:
# Blastoff!

# An explanation of your choice for what to call for input of zero.

# - because COUNTDOWN IS A DEFAULT ( and COUNT_UP IS RARELY USED ) for zero input values I used countdown
# - I assumed that zero input means that user wants an immediate trigger

# 2. Write your own unique Python program that has a runtime error. Do not copy the program from 
# your textbook or the Internet. Provide the following.

# The code of your program.
start_point = None
start_point_str = input('Please type counter start point (must be integer) = ')

try:
   start_point = int(start_point_str)
except ValueError:
   print("That's not an int!")

if start_point is not None:
     if start_point >= 0:    # if start_point == 0 call count_down
          countdown(start_point)
     else:
         count_up(start_point)



# print(len(1234))
x = 0
print (5/x)

# Output demonstrating the runtime error, including the error message.

# it prints
# Traceback (most recent call last):
#   File "/Users/myfamily/Documents/00CurWorks/AllCode/Python/Hello/u3learningGuide.py", line 52, in <module>
#     print(len(1234))
# TypeError: object of type 'int' has no len()

# An explanation of the error message:
# it means that len can not be used with integer values and most probably it can't be used with other numeric values as well

# An explanation of how to fix the error.
# if we want to know how many digits our number has we could convert it to string as follows:
print( len( str(1234) ) )