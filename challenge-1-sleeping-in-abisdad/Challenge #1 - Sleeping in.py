# Challenge #1 - Sleeping in
# https://github.com/GIHS-Raspberry-Pi-Club/challenge-1-sleeping-in-abisdad
# Code to determine if I can sleep in...
# By Rob Thomas
# 30/10/2017
# Ver 1.0

def sleepIn(weekday, holiday):
    if holiday or not weekday:
        print("Zzzzzzz...... :-)", end=" ")
        return True
    else:
        print("DING! DING! DING!",end=" ")
        return False

print(sleepIn(False, False))
print(sleepIn(True, False))
print(sleepIn(False, True))
