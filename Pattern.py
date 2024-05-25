# Number of rows for the pattern
rows = 5

# Loop to print the pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
