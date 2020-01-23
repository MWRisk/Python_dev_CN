#Let’s create a ticket machine for a cinema
#Write an if statement that checks the ages of cinema goers, and display the ticket prices:
#- Child (below age of 18): £8
#- Adult (18+): £10.95
#- Senior (60+): £7.50
#First thing’s first
#Functions
#Python

age = 18
​
if age > 59:
    print("Senior ticket: £7.50.")
​
elif age < 18:
    print("Child ticket: £8.00")   

else:
    print("Adult ticket: £10.95")




#age = 15
​
#if age < 18:
 #   print("Your age is {}.Child ticket is £8".format(age))
#elif age >= 18 and age < 60 :
 #   print("Your age is {}.Adult ticket is £10.95".format(age))
#else:
 #   print("Your age is {}. Senior ticket is £7.50".format(age))

