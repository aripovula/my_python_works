
# 1. true ONLY if FIRST letter is lowercase, otherwise false, because it returns in first iteration either way
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print( "1 - Cs", any_lowercase1("Cs") ) # 1 - Cs False
print( "1 - sC", any_lowercase1("sC") ) # 1 - sC True

# 2. ALWAYS returns TRUE regardless of argument value as 'c' is not variable but a lowercase value
# this function is totally wrong. See function call results below - both return 'TRUE'
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print( "2 - Cs", any_lowercase2("Cs") ) # 2 - Cs True
print( "2 - sC", any_lowercase2("sC") ) # 2 - sC True

# 3. true ONLY if LAST letter is lowercase, otherwise false, because it returns only when iteration finishes
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print( "3 - Cs", any_lowercase3("Cs") )  # 3 - Cs True
print( "3 - sC", any_lowercase3("sC") )  # 3 - sC False

# 4. if ANY letter is lowercase it returns true, otherwise false because once flag's value is true its value is always true
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()   # once flag's value is true c.islower() is never reached and just returns true
    return flag

print( "4 - Cs", any_lowercase4("Cs") )  # 4 - Cs True
print( "4 - sC", any_lowercase4("sC") )  # 4 - sC True
print( "4 - s", any_lowercase4("s") )  # 4 - s True
print( "4 - C", any_lowercase4("C") )  # 4 - C False

# 5. if ALL letters are lower case returns true. If any letter is upper case returns false because 
# true is returned after loop ends. False is returned when any capital letter is found inside of loop.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print( "5 - Cs", any_lowercase5("Cs") )  # 5 - Cs False
print( "5 - smallCap", any_lowercase5("smallCap") )  # 5 - smallCap False
print( "5 - CC", any_lowercase5("CC") )  # 5 - CC False
print( "5 - small", any_lowercase5("small") )  # 5 - small True
