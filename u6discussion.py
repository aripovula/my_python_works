# Describe the difference between objects and values using the terms “equivalent” and 
# “identical”. Illustrate the difference using your own examples with Python lists and 
# the “is” operator.  

# The difference between objects and values is that object is always of type object while 
# values can be of any type. Values can also be objects.

list_zero = ['a', 'b'] 
list_one = ['a', 'b', 'c']
list_two = ['a', 'b', 'c']

# object “equivalence” is checked using operands '=='
# objects are “equivalent” if object1 == object2 is true

print (list_zero == list_one) # false
print (list_one == list_two) # true

# objects are “identical” if object1 is object2 is true - i.e. we use the is operator

# objects can be "identical" only if those objects are “equivalent” as 
# not “equivalent” objects are clearly different objects.
print (list_zero is list_one)  # false - can't be true is these two are not “equivalent”
print (list_one is list_two) # false

list_three = list_one
print (list_one is list_three) # true

# Describe the relationship between objects, references, and aliasing. Again, create your 
# own examples with Python lists.

# The association of a variable with an object is called a reference (Think Python, Downey A.). 
# In our case ['a', 'b'] and ['a', 'b', 'c'] are list objects. "list_zero" variable refers to 
# ['a', 'b'] and list_one, list_two and list_three all refer to objects with value of ['a', 'b', 'c'].
# But they do not necessarily refer to the same object. 

# An object with more than one reference has more than one name, so we say that the object
# is aliased (Think Python, Downey A.). In our case list_one and list_three refer to same object in memory.
# list_one and list_two refer to different objects in memory which coincidentally have the same value.


# Finally, create your own example of a function that modifies a list passed in as an 
# argument. Describe what your function does in terms of arguments, parameters, objects, 
# and references. 

# this code converts text to list and passes to function as argument.
# The function removes all small case letters and adds it to a new list.
# At the end it returns a list of passed argument as a string and letters left as two values of a new list.
def remove_small_case_letters_and_sort_append_both(ts):
    t_new = []
    for t in ts:
        if t.isupper():
            t_new.append(t)
    t_new.sort()
    t2_new = [''.join(ts), '-'.join(t_new) ]
    return t2_new 

text = 'LEAVE UPPER CASE TEXT and remove small case letters'
ts = list(text)   # converts string to arrays of letters
# ts = text.split()  - this would split sentence to list of words, not letters
new_string = remove_small_case_letters_and_sort_append_both(ts)
print(new_string)

