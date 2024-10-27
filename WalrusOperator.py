# most simple example
print(a := 10)    # can't do this before but after 3.8 version it can be done i.e. assignment within expression

# example 2
arr = [1, 2, 3, 4, 5]
while(n := len(arr)) > 0:
    print(f"Popped : {arr.pop()}")

# example 3
foods = []
while(food := input("What food do you like?") != "quit"):
    foods.append(food)
print(foods)