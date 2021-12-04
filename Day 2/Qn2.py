# find BMI of a person where  take mass and height as input from the user.
# formula   BMI = ma in kg /(height in m)2

Mass = int(input("Enter mass of a person in kg"))
height = float(input("Enter height of a person in m"))
BMI=Mass/ (height)**2
print(f"The BMI of a person is {BMI}")