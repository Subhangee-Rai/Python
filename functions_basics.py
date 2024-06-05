# printing multiplication table
def table(num):
    print("Table of ", num, " is:\n")
    for i in range(1, 11):
        print(num, " x ", i, " = ", num*i)


table(5)


# printing average of values in a list
def average(l):
    suma = 0
    for i in l:
        suma += i
    avg = suma/len(l)
    print("Average of list elements is ", avg)


average([20, 40, 50, 10, 63])


# basic calculator
def calci(a, b, o):
    match o:
        case '+':
            print(a, " + ", b, " = ", (a+b))
        case '-':
            print(a, " - ", b, " = ", (a - b))
        case '*':
            print(a, " * ", b, " = ", (a * b))
        case '/':
            print(a, " / ", b, " = ", (a / b))


calci(20, 10, '+')
calci(20, 10, '/')


# factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)


result = fact(5)
print("Factorial of 5 is", result)


# fibonacci
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def print_fib_sequence(n):
    for i in range(n):
        print(fib(i), end=" ")


print_fib_sequence(7)
