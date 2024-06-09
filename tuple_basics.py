# tuple creation
tup = (1,2,3,4)
print(tup)

# single element tuple
t = (3,)
print(t)

# applying operations { indirect method }
tpl = (10, 30, 1, 50, 2, 100)
print(tpl)
l = list(tpl)
for i in l:
    if i == l[2]:
        l[2] = 404

l.append(999)
tpl = tuple(l)
print(tpl)

# tuple methods

print("Count: ", tpl.count(100))
print("Index: ", tpl.index(30, 0, 2))
print("Length: ", len(tpl))