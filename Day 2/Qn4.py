# N students take K apples and distribute them among each other evenly. The remaining
#(the indivisible) part remains in the basket. How many apples will each single student
#get? How many apples will remain in the basket? The program reads the numbers N and K. 

Student = int(input("Enter the number of Students: "))
Apple = int(input("Enter the Number of Apples: "))
Distribute = Apple//Student
Remaning = Apple%Student
print(F"Each student gets {Distribute} No. of apples and {Remaning} no. of apples are remaning")