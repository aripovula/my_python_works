

# Example 1: Define a function that takes an argument. Call the function. Identify what 
# code is the argument and what code is the parameter.

def call_me_with_argument(param) :
    print(param)

call_me_with_argument('* * * *')
call_me_with_argument('According to https://www.python.org/dev/peps/pep-0008/')
call_me_with_argument('function and variable names should be lowercase, with words separated by')
call_me_with_argument('underscores as necessary to improve readability.')
call_me_with_argument('See "Function and Variable Names" in web-page with above link.')
call_me_with_argument('* * * *')

# "param" in function definition is a paramater.
# All text being used to call the function above are arguments.


# Example 2: Call your function from Example 1 three times with different kinds of 
# arguments: a value, a variable, and an expression. Identify which kind of argument is which. 

call_me_with_argument(' I am a call with VALUE')
with_variable = ' I am a call with VARIABLE'
call_me_with_argument( with_variable )
with_expression1 = ' I am a' + ' call with'
with_expression2 = ' EXPRESSION ' + 'too'
call_me_with_argument(with_expression1 + with_expression2)
call_me_with_argument( 2 + 3 )   # another call with expression

# Example 3: Create a function with a local variable. Show what happens when you try to use that 
# variable outside the function. Explain the results.

def function_with_local_variable(unique_param) :
    a_number = int(unique_param)
    print(a_number)

# print(a_number)
# prints following error:
#     print(a_number)
#  NameError: name 'a_number' is not defined


# Example 4: Create a function that takes an argument. Give the function parameter a unique name. Show 
# what happens when you try to use that parameter name outside the function. Explain the results.

# print(unique_param)   # uses function defined in Example 3
# prints following error:
#    print(unique_param)
# NameError: name 'unique_param' is not defined

# Example 5: Show what happens when a variable defined outside a function has the same name as a 
# local variable inside a function. Explain what happens to the value of each variable as the program runs.

abc = 'DEF'
print ('outer 1 - ' + abc)
def same_name_inner_and_outer_variables() :
    abc = 'XYZ'
    print ('inner - ' + abc)

same_name_inner_and_outer_variables()
print ('outer 2 - ' + abc)
#  it prints
#  outer 1 - DEF
#  inner - XYZ
#  outer 2 - DEF
