# a program to wish good morning/afternoon/evening/night based on current system time
import time
# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)

timestamp = int(time.strftime('%H'))    # gives time in string so typecasted
if 0 <= timestamp < 12:
    print("Good Morning")
elif 12 <= timestamp < 16:
    print("Good afternoon")
elif 16 <= timestamp < 22:
    print("Good evening")
else:
    print("Good night")
