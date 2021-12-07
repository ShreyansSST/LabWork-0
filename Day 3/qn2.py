# WAP which accepts marks of four subjects and display total marks, percentage and grade. 
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail .

Subject1 = int(input("Enter marks in First Subject: "))
Subject2 = int(input("Enter marks in Second Subject: "))
Subject3 = int(input("Enter marks in Third Subject: "))
Subject4 = int(input("Enter marks in Four Subject: "))
Total_Mark = Subject1 + Subject2 + Subject3 + Subject4
print(f"The Total marks you scored is {Total_Mark}")
percentage = (Total_Mark/400)*100
print(f"You scored {percentage}%")
if percentage>70 :
    print("You scored Distinction.")
elif percentage>60:
    print("YOu scored First Grade.")
elif percentage>40:
    print("You Passed.")
else:
    print("You Failed.")