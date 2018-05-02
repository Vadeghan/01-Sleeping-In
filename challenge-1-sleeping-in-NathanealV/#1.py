import os, time
def sleep_in(weekday, holiday, wednesday):
    if wednesday == "True" and weekday == "False":
        print("Error Wednesday is a weekday. Please try again.")
        return None
    elif holiday == "True" or wednesday == "True":
        print("Sure sleep in!")
        return True
    elif weekday == "True" and holiday != "True":
        print("Don't sleep in")
        return False
    elif weekday == "False" and holiday == "False" and wednesday == "False":
        print("Sure sleep in!")
        return True
    else:
        print("Don't sleep in")
        return False

while True:
    print("Type True or False for each parameter")
    weekd = input("Weekday: ")
    holid = input("Holiday: ")
    wednesd = input("Wednesday: ")
    print("////////////////////////")
    sleep_in(weekd, holid, wednesd)
    print("///////////////////////")
    print()
    print()
    print("-----------------------------")
    print("Restarting app in 3...")
    time.sleep(1)
    print("Restarting app in 2...")
    time.sleep(1)
    print("Restarting app in 1...")
    time.sleep(1)
    os.system("cls")
    
