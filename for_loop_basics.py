# iterating a list using for loop
colors = ["red", "green", "yellow"]
for color in colors:
    print(color, end=" ")

# displaying a star pattern using for loop
for i in range(0, 5):
    for j in range(1, i+1):
        print("*", end=" ")
    print("\n")

# displaying multiplication table of using for loop
n = 5
for i in range(1, 11):
    print(n, " x ", i, " = ", n*i, "\n")


# Checking even or odd using for loop
n = [2, 3, 4, 5, 6]
for i in n:
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, "is odd")

# Printing first 20 odd numbers using for loop
for i in range(1, 20, 2):
    print(i)
