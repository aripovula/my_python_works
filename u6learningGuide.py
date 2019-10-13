# Part 1

def remove_three_elements_sort_add_three_words_convert_to_string(ts):
    first = ts.pop(1)
    ts.remove('but')
    del ts[3]
    
    ts.sort()

    ts.append('NEW')

    ts = ts + ['WORDS']

    ts2 = ["WERE", "ADDED"]

    ts.extend(ts2)
    
    return ' '.join(ts)

text = 'Delete three words from the list, but delete each one using a different kind of Python operation'
ts = text.split()
new_string = remove_three_elements_sort_add_three_words_convert_to_string(ts)
print(new_string)


# Part 2

a_list = ['a', 'b']
# Nested lists
nested = [a_list, ['c', 'd', [ 'ea', 'eb' ] ] ] 
print( nested[1][2][0])  # prints 'ea'
# The “*” operator
print (a_list * 3) #  prints "['a', 'b', 'a', 'b', 'a', 'b']"
print (nested * 1) #  prints "[['a', 'b'], ['c', 'd', ['ea', 'eb']]]"
# List slices 
print( nested[:1] )  # [['a', 'b']]
print( nested[1:] ) # [['c', 'd', ['ea', 'eb']]]
print( nested[1:2] ) # [['c', 'd', ['ea', 'eb']]]
# The “+=” operator 
symbols_length = 0
for y in nested:
    symbols_length += len(y)
print ( symbols_length )
# A list filter 
def even_numbers(ts):
    new_ts = []
    for y in ts:
        print (y,' ', y%2)
        if (y%2 == 0):
            new_ts.append(y)
    return new_ts
numbers = [1, 2, 3, 4, 5, 8, 11, 15, 18]

print( even_numbers(numbers) )   # prints [2, 4, 8, 18]

# A list operation that is legal but does the "wrong" thing, not what the programmer expects 
a_list = [1, 2, 3]
a_list2 = a_list.append(22)
print(a_list2)  # prints None - it is legal, but has no effect as return type of append is void (returns None)
a_list + [4, 5]  # this is legal but has no effect as resulting value should have been assigned to another variable
print (a_list)

# Part 3

# Describe your experience so far with peer assessment of Programming Assignments.

# How do you feel about the aspect assessments and feedback you have received from your peers?
# In almost all cases assessment and feedback have been quite reasonable and constructive. Some student provide
# constructive and useful feedbacks.

# How do you think your peers feel about the aspect assessments and feedback you provided them?
# I have been trying to be as objective as possible and I hope they feel that provided feedback is reasonable and just.

for fruit in ["banana", "apple", "quince"]:
    print (fruit)

my_list = [3, 2, 1]
print(my_list.sort())

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[2::2]))

# mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
# a=0
# while a < 8:
#     print(mylist[a],)
#     a = a + 2

n = 10000
count = 0
while n:
    count = count + 1
    n = n / 10
    n=int(n)
print(count)

bb = 0
if bb:
    print('abc')

def print_n(s, n):
     if n > 0:
          print(s)
          print_n(s, n-1)
     return n
n = 3
while print_n("hi", n):
     print_n("there!", n)
     n = 0