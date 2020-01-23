#create a variable called num. check if the number is a palindrome...and

num = 245
#[] refer to indexing
#print(str(245)[::-1])

num = 245

if str(num)[::-1] == str(num):
    print("Palindrome")
else:
    print("not a palindrome")

