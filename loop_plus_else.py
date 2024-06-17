# In this case the else block will run, coz loop ended
for i in range(6):
    print(i)

else:
    print("Loop ended!!!")

# In this case the else block will not run, coz the loop didn't end it break in between
for i in range(6):
    if i == 4:
        break
    print(i)

else:
    print("Loop ended!!!")

