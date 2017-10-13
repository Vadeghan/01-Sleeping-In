# Challenge #1 - Sleeping in

Like this challenge, sleeping should be very easy for you. Unfortunatly, we aren't always in a position to do so.

> For this week's challenge, you must write a script that takes two arguments (`weekday` and `holiday`), to determine whether or not it is a suitable day for a sleep in.

#### Input:
Both arguments (or parameters) will be inputted as boolean values. Therefore, the parameter weekday will be True if it is a `weekday`, and the parameter `holiday` will be True if we are on holidays, and vice versa.

#### Output:
Like, your input, your output must also be a boolean value, in this case. You must return True if it is either not a weekday, if it is holiday time, or if it happens to be both.

`sleepIn(weekday, holiday) ==> output`

#### Examples:
Try out these sample tests to check if your code is working properly:
```
sleepIn(False, False) ==> True
sleepIn(True, False) ==> False
sleepIn(False, True) ==> True
```

## Extension
Let's make this code even more useful by adding another parameter into the mix. Since school for us usually starts an hour later on Wednesdays, lets add a parameter called `wednesday`, which if True, also makes the output true. There's one catch. Because Wednesday is a weekday, if the user sets `wednesday` to be True, while setting  `weekday` to be False, they have just performed the impossible. As a result, you should return a None value, or the equivelent of that in your selected programming language. This should be done whether or not `holiday` is True.

```
sleepIn(weekday, holiday, wednesday) ==> output

sleepIn(False, False, True) ==> True
sleepIn(True, False, True) ==> True
sleepIn(False, True, True) ==> None
sleepIn(False, False, True) ==> None
```

### Acknowledgments
* Thanks to CodingBat for the original idea behind this challenge
* Repository created by Javad Hamidi on behalf of the GIHS Raspberry Pi Club
