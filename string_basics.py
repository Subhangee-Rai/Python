# str = input("Enter a string: ")
str11 = "Hello"
print("Using for loop to display string str")
for c in str11:
    print(c, sep="")


print("\nString slicing")
str1 = "Somi, Shubhi, Kishu"
print("Length of string is: ", len(str1))
print(str1[0:4])
print(str1[6:12])
print(str1[14:19])
print(str1[:])
print(str1[0:])
print(str1[-19:])

# String indices ( both positive and negative )
#  0  1  2  3  4
#  h  e  l  l  o
# -5 -4 -3 -2 -1

# strings are immutable
print("String methods")
a = "Flower Pot"
print(a.lower())        # doesn't change the same string, generate a new string
print(a.upper())
print(a.isalpha())
print(a.isalnum())
print(a.isascii())
print(a.strip("!"))
print(a.split("!"))     # change the string into a list ( string remains same )
print("shubhi".capitalize())
print(a.center(30))     # adds spaces before the string to align it in the center
print(a.count('e'))
print(a.index("ot"))
