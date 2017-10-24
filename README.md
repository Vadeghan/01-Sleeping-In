# Challenge #1 - Sleeping in

Like this challenge, sleeping should be very easy for you. Unfortunately, we aren't always in a position to do so.

> For this week's challenge, you must write a script that takes two arguments (`weekday` and `holiday`), to determine whether or not it is a suitable day for a sleep in.

#### Input:
Both arguments (or parameters) will be inputted as boolean values. The parameter `weekday` will be True if it is a weekday, and the parameter `holiday` will be True if we are on holidays, and vice versa.

#### Output:
Like, your input, your output must also be a boolean value. *You must return True if it is either not a weekday, if it is holiday time, or if it happens to be both, otherwise return False.*

`sleep_in(weekday, holiday) ==> output`

#### Examples:
Try out these sample tests to check if your code is working properly:
```
sleep_in(False, False) ==> True
sleep_in(True, False) ==> False
sleep_in(False, True) ==> True
```

## Extension
Let's make this code even more useful by adding another parameter into the mix. Since school for us usually starts an hour later on Wednesdays, let's add an argument called `wednesday`, which if True, also makes the output True. 

There's one catch. Because Wednesday is a weekday, if the user sets `wednesday` to be True, while setting  `weekday` to be False, they have just performed an error on their part. As a result, you should return a None value, or the equivalent of that in your selected programming language. This should be done whether or not `holiday` is True.

```
sleep_in(weekday, holiday, wednesday) ==> output

sleep_in(False, False, True) ==> True
sleep_in(True, False, True) ==> True
sleep_in(False, True, True) ==> None
sleep_in(False, False, True) ==> None
```

### Acknowledgments
* Thanks to CodingBat for the original idea behind this challenge
* Repository created by Javad Hamidi on behalf of the GIHS Raspberry Pi Club
