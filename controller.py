import pantilthat
import time

# time 1 sec to give it some lag
# pantithat is a 
pantilthat.idle_timeout(.5)

pantilthat.tilt(90)
time.sleep(1)
pantilthat.tilt(0)
time.sleep(1)
pantilthat.tilt(-90)
time.sleep(1)
pantilthat.tilt(0)
time.sleep(1)


# When the robot swings arm in each direction with a 1sec lag.
pantilthat.pan(90)
time.sleep(1)
pantilthat.pan(0)
time.sleep(1)
pantilthat.pan(-90)
time.sleep(1)
pantilthat.pan(0)




print('Complete')