# tryme4.py

def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()    #9
    nine_lines()    # 18
    three_lines()   # 21
    three_lines()   # 24
    new_line()      # 25

# these lines should NOT be indented as otherwise it may be treated as part of last function above
print('Printing nine lines:') 
nine_lines()
print('') # to add separating line
print('Calling clearScreen():')
clear_screen()
