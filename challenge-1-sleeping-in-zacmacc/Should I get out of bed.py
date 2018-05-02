'''
Should I get out of bed.
By Zac McDonnell
26/10/17

email me: contactzacmac@gmail.com
if there is any issues you might have found or ways I can
improve this code
'''

#defines variables for later use
wednesdays = False
holidays = False
weekdays = False

#function where it decideds what day it is
def sleep_in(weekday, holiday, wednesday):
    if wednesday: #wednesday morning
        print("You can sleep in")
    elif weekday == False: #weekend
        print("You can sleep in")
    elif holiday: #holiday
        print("You can sleep in")
    else:
        print("GET OUT OF BED") #weekday

#this is where I ask the user what day of the week it is

#If it is the holidays it doesn't matter what day it is so I dont ask the user.
holys = input("Is it the holidays? eg True or False: ")
if holys == "True":
    holidays = True
else:
    wed = input("Is it a wednesday? eg True or False: ")
    if wed == "True":
        wednesdays = True # Here I set wednesdays to trigger weekdays and wednesdays removing user error
        weekdays = True
    else:
        week = input("Is it a weekday? eg True or False: ") # If the user answers False then I assume its the weekend
        if week == "True":
            weekdays = True

sleep_in(weekdays, holidays, wednesdays)

