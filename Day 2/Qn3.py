# given the integer N -  the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock ?

NoOfMinutes  = int(input("enter the minute passed since midnight"))
Hours = (NoOfMinutes//60)
Minutes = (NoOfMinutes%60)
print (F"the hours is {Hours}")
print  (F"the minutes is {Minutes}")
print (F"{Hours}:{Minutes}")