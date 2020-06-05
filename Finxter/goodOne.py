"""
UNique puzzle
"""
# ELse loop is executed only when the while loop condition is not meet.
# Else loop is not executed after the break statement has been executed
stringy = "g"

index_value = 5

while index_value > 3:
    index_value -= 1
    stringy += "o"
    if index_value == 3:
        break
else:
    stringy += "d"

print(stringy)

"""
Unique puzzle : 2
"""

i = 5

def f(arg=i):
    print(arg)

i = 6
f() # not passing the re-initialized value to the func, so it takes the default value during declaration.

# Parameter test
def add(a = 0, b= 1):
    return a+b

print(add(add(add()))) # paramerter will be passed to a and b will remain as 1