# factorial

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)


res = fact(5)
print("Factorial of 5 is:", res)

# fibonacci series
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print("Fibonacci series:", end=" ")
for i in range(0, 5):
    res = fib(i)
    print(res, end=" ")
