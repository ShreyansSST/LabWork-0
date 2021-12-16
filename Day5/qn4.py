#Write a Python program to construct the following pattern, using a nested for loop.

rows = int(input("Enter number of rows:"))
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print("*", end='*')
    print()

for i in range(rows, 1, -1):
    for j in range(1, i):
        print("*", end='*')
    print()
