#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
# How long will the bus journey take? Alternatively, you could run to university. 
#You jog the first mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus?

Distance = 4
BusSpeed = 25/60    #converted mph to miles per min.
WaitTime = 2
Stops = 10
Waiting = WaitTime * Stops
BusTime = BusSpeed * Distance
BusTotalTime = BusTime + Waiting

speed1 = 7/60       #converted mph to miles per min.
speed2 = 15/60
time_7mpm = speed1*2
time_15mpm = speed2*2
jog_totaltime = time_7mpm + time_15mpm

if BusTotalTime>jog_totaltime:
    print(f"Bus will be Faster than Jogging.")
elif BusTotalTime<jog_totaltime:
    print(f"Jogging will be Faster than Travelling by Bus.")
else:
    print(f"Both Jogging and Travelling by Bus take same time.")