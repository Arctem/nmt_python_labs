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
#traction = 100
#circum = 2*math.pi*0.1
#max_speed = 500
#accel = 1

for i in range(10):
    speed = speed + accel * (max_speed - speed)
    ideal = speed * circum
    actual = newspeed(actual, ideal, traction)
    total += actual
    print('{:.2f}'.format(total))
