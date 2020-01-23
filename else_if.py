age = 25
country = UK

#if age >= 18 and age < 25:
    #print("could I see your ID?")
#elif age >= 25:
    #print("I can serve you")
#else:
    #print("You aren't old enough")

if age >= 18 and age <25 and country.upper() == "UK":
    print("could I see your ID?)
elif age >= 25 and country.upper() == "UK":
    print("Happy to serve you boss")
elif age >= 21 and country.upper() == "USA":
    print()
