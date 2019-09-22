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
# Output for the following input: a positive number, a negative number, and zero.
# An explanation of your choice for what to call for input of zero.

start_point_str = input('Please type counter start point (must be integer) = ')
start_point = int(start_point_str) # ideally we should verify that it is indeed an integer using try: except
if start_point >= 0:    # if start_point == 0 call count_down
    countdown(start_point)
else:
    count_up(start_point)

# 2. Write your own unique Python program that has a runtime error. Do not copy the program from your textbook or the Internet. Provide the following.

# The code of your program.
# Output demonstrating the runtime error, including the error message.
# An explanation of the error message.
# An explanation of how to fix the error.

print(len(1234))

# it prints
# Traceback (most recent call last):
#   File "/Users/myfamily/Documents/00CurWorks/AllCode/Python/Hello/u3learningGuide.py", line 52, in <module>
#     print(len(1234))
# TypeError: object of type 'int' has no len()