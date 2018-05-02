def sleepin():
    mon = ("monday")
    tues = ("tuesday")
    wed = ("wednesday")
    thurs = ("thursday")
    fri = ("friday")
    sat = ("saturday")
    sun = ("sunday")
    
    day = input("What day is it? ")
    
    if day == mon or day == tues or day == wed or day == thurs or day == fri:
        kindofday = input("What kind of day is it (holiday or weekday)? ")

        wd =("weekday")
        hd = ("holiday")

        if kindofday == wd:
            print("You cannot sleep in. Sorry!")

        elif kindofday == hd:
            print("You can sleep in. Woohoo!!!")

        else:
            print("You entered something incorrect. Go back and try again.")
    elif day == sat or day == sun:
        print("You can sleep in! Woohoo!")
            
    else:
        print("You entered something incorrectly. Try again.")

sleepin()
