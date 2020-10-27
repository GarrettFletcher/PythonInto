mathclass = [19, 21, 17, 20, 20, 18, 19, 22, 23, 18, 59]
def add(a,b):
    return a+b
import functools
print(functools.reduce(add, mathclass))
print("Is the total age of the class!")