# convert seconds to day, hours, minutes 
sec = int(input("enter seconds"))
day = sec/(60*60*24)
hrs = sec/(60*60)
min = sec/(60)
print("seconds in day is {}." .format(day))
print('seconds in hour is {}.'.format(hrs))
print("seconds in minute is {}.".format(min))
