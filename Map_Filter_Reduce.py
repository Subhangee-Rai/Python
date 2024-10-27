# Map : Applies the function (cube) to all iterables ( all elements of list l)
# and returns a new map (newl, typecasted into list)
def cube(x):
    return x*x*x


l = [1, 2, 3, 4, 5]
newl = list(map(cube, l))
print(newl)

# Filter: filters & give the elements that satisfies the condition, in form of objects
def greater(x):
    return x > 4


newl1 = list(filter(greater, l))
print(newl1)

# Reduce : will apply the function to pairs of iterable and then keep doing this till end and returns a single value
from functools import reduce
newl2 = reduce(lambda x,y:x+y, l)
print(newl2)

# 'is' & '==' comparison
# a = [1,2,3]   # False
# b = [1,2,3]   # True

a = 4    # True or False
b = 4   # True
print(a is b)    # exact location in memory is compared
print(a == b)    # values given is compared

