# Challenge #1 - Sleeping in
# https://github.com/GIHS-Raspberry-Pi-Club/challenge-1-sleeping-in-abisdad
# Code to determine if I can sleep in...
# By Rob Thomas
# 30/10/2017
# Ver 2.0

def sleepIn(weekday, holiday, wednesday):
    if holiday or not weekday or wednesday:
        print("Zzzzzzz...... :-)", end=" ")
        return True
    else:
        print("DING! DING! DING!",end=" ")
        return False

print(sleepIn(False, False, True))
print(sleepIn(True, False, True))
print(sleepIn(False, True, True))
print(sleepIn(True, False, False))
print(sleepIn(True, True, True))
