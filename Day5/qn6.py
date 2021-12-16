#Write a Python Program to count the number of even and odd numbers from a series of number.
num = [11,22,33,44,55,66,77,88,99]
odd,even = 0,0
for i in range(len(num)):
    w = num[i]
    if w%2 == 0:
        odd = odd + 1
    else:
        even = even + 1
print(f"Total Number of Even are {even} and odd are {odd} ")