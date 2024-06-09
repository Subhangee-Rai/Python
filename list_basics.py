# making a list
l = [10,30,40,20,60,100]

# traversing list
for i in l:
    print(i, end=" ")

# list slicing
l1 = l[2:3]
print("\n")
print(l1)

l2 = l[0:]
print(l2)

# list methods
l.append(109)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.insert(3, 1000)
print(l)

l_copy = l.copy()
print(l_copy)

print(l.count(10))

# list comprehension
l_comp = [i for i in range(6)]
print(l_comp)

# using functions
def avg(arg):
    sum = 0
    for i in arg:
        sum = sum+i
    print("Average: ",sum/len(arg))

avg(l_comp)