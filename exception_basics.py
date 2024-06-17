# Exception in basic multiplication table of a number
try:
    n = int(input("Enter the number: "))
    print(f"Multiplication table of {n} is:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
except Exception as e:
    print(f"An error occurred: {e}")

print("Ended")


# different types of error
try:
    n = int(input("Enter the number: "))
    a = [6, 3]
    print(a[n])
except ValueError:
    print("Invalid value entered")
except IndexError:
    print("Index not in range")
except OverflowError:
    print("Overflowed")
except RuntimeError:
    print("Run time error occurred")

# Finally keyword


def display_element(i):
    l = [1, 2, 3, 4, 5, 6]
    try:
        print(f"List element at index {i} is {l[i]}")
        return 0
    except:
        print("Error occurred")
        return -1
    finally:
        print("Ended")


result = display_element(0)
print(f"Result of the search is {result}")
result = display_element(10)
print(f"Result of the search is {result}")

# custom errors
n = int(input("Enter a number between 4 to 16: "))
if n < 4 or n > 16:
    raise ValueError("Value should be between 4 & 16")

