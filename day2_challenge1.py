#create code to show where you are during the day using 3 variables

time = 100
place_of_work = "Manchester"
town_of_home = "Rossendale"

if time > 1800 or time < 800:
    print("I am in " + town_of_home)
elif time >= 900 and time <= 1700:
    print("I am in " + place_of_work)
else:
    print("I am commuting")

