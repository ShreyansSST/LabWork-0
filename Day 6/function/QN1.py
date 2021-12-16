# Write a Python function to find the Max of three numbers.
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third nmber:"))

def f():
    if(n1>=n2) and (n1>=n3):
        l=n1
    elif(n2>=n1) and (n2>n3):
        l=n2
    else:
        l=n3
    print("largest number among the three is",l)
f()    

