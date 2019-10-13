# 1. Modify the program so that it prints "Ouack" and "Quack" but leaves the other names the same.

def ducklings():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            # uses f literal
            print( f"{letter}u{suffix}")
        else:
            # left as it was
            print(letter + suffix)

ducklings()

# prints
# Jack
# Kack
# Lack
# Mack
# Nack
# Ouack
# Pack
# Quack

# 2. Give at least three examples that show different features of string slices. Describe the feature.

s = 'Slicing string'
# We can also use negative numbers. When negative it starts counting from end in backward direction.
# Therefore, abs value of first number should be greater.

print(s[-6:-1])    # prints 'strin'

# We can also mix. Positive numbers start from beginning. Negative numbers start from end backwards.

print(s[1:-1])    # prints 'licing strin'

# or visa versa

print(s[-10:10])    # prints 'ing st'

# split is a powerful tool that convers text to array of words.

t = s.split()
print(t[0])    # prints 'Slicing'
