#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR".
#without checking gender value is correct or not
age = int(input("Enter your age:"))
gender = input("ENter your Gender(M or F):")

while gender == "M":
    if age >20 and age <40:
        print("You may work either in anywhere.")
    elif age>=40 and age<60:
        print("You can work only in urban areas.")
    else:
        print("Error")
    break
else:
    print("You will work only in urban areas.")

#with checking gender value is correct.
if gender == "M" or gender == "F":
    if gender == "M":
        if age >20 and age <40:
            print("You may work either in anywhere.")
        elif age>=40 and age<60:
            print("You can work only in urban areas.")
        else:
            print("Error")
    else:
        print("You will work only in urban areas.")
    
else:
    print("You entered Wrong Gender Value")