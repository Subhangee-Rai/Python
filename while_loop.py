# printing even numbers from 1 to 10
i = 1
while i < 11:
    if i % 2 == 0:
        print(i)
    i = i + 1

# using while loop to verify equation
n = 2
x = 1
while ((n*(x ** 2)) - (n*x) + 1) == 1:
    print("correct")
    n = n+1
    x = x+1
