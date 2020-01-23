#Create a variable called num. If num is div by 3 print "fizz", if div by 5 print buz, of both, fizz buzz. otherwise print num.

num = 9

if num % 3 == 0 and num % 5 == 0:
    print("Fizz buzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print("num")
