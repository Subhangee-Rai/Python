# creating a set
s1 = {1, 2, 3, "Hello", 2, 3}
print(s1)

# empty
s = {}  # is an empty dictionary
print(type(s))
s = set()   # is an empty set
print(type(s))

# accessing set elements
for i in s1:
    print(i, sep="-", end=" ")
print(end="\n")


# set methods
s1 = {1, 2, 344, "a", "b"}
s2 = {"a", "b", 2.1, 4.0}

# union
print(s1.union(s2))     # s1 & s2 will remain same

# update
s3 = {0, 1.1, 1}
s3.update(s2)   # s3 is updated with the values of s2 ; union update
print(s3)

# intersection
print(s1.intersection(s2))

# Intersection update
s3.intersection_update(s1)
print(s3)

# difference
print(s1.difference(s2))

# symmetric difference
print(s1.symmetric_difference(s2))

# disjoint checking
print(s3.isdisjoint(s1))

# remove and discard
s1.remove(2)
print(s1)

s2.discard(304)
print(s2)