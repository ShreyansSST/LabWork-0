#Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number. 

def max(x,y):
    if x>y:
        return x
    return y
def max(x,y,z):
    return max(x,max(y,z))  
print("max number is ",max(3,6,90))          