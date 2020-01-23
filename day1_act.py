# 1: Create a program that stores someone's name, age and favourite colour tht prints this out in a complete sentence
name = "Matt"
age = 39
fav_colour = "blue"

print("My name is " + name + ", I am " + str(age) + " and my favourite colour is " + fav_colour + ".")
#requires conversion of integer to string using the str() 

# 2: Create a program that stores what you ate for breakfast, lunch and dinnner and print these out

breakfast = "cornflakes"
lunch = "sandwich"
dinner = "curry"

print("todays meals were " + breakfast + ", " + lunch + " and " + dinner)

#Change variables - to show what you will eat tomorrow

breakfast = "cornflakes"
lunch = "burger"
dinner = "pasta"

print("tomorrows meals are " + breakfast + ", " + lunch + " and " + dinner)

# Leona suggested using the format method as well to get used to it:

print("for breakfast today I had {}".format(breakfast) + ", lunch was {}".format(lunch) + " and for dinner I ate {}".format(dinner) + ".")

# 3 Create a program that calculates how many days old you are - Hint: Import a library...
import datetime
from datetime import date
today = date.today()
age = date.today() - date(1980,5,20)
print(age.days)
days = (age.days)
print(age)