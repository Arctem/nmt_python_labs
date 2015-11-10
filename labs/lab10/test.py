import math

def newspeed(cur, ideal, traction):
    diff = ideal - cur
    if diff < traction:
        return ideal
    else:
        return cur + traction + 0.5*(diff - traction)

actual = 0
total = 0
speed = 0

#rabbit
traction = 0
circum = 2*math.pi*0.5
max_speed = 1000
accel = 0.1

#hare
traction = 100
circum = 2*math.pi*0.1
max_speed = 500
accel = 1

#detailed
traction = 10
circum = 2
max_speed = 100
accel = 0.5

for i in range(10):
    total += actual
    speed = speed + accel * (max_speed - speed)
    ideal = speed * circum
    actual = newspeed(actual, ideal, traction)
    #print('{:.2f}'.format(total))
    print('{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}'.format(total, actual, ideal, speed))
