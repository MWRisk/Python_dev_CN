#Cash machine time. Let’s create one that :
#Takes an input of pin number and amount
#Prints dispensing cash if the pin number is correct and there’s enough money to withdraw} Displays the new bank balance
#Be creative!

balance = 4000
correctpin = 2222 

# def check(pin, amount):
#     if pin == correctpin and amount <= balance:
#         print("dispensing cash - £" + str(amount))
#     elif balance < amount:
#         print("Not enough dough in the bakery")
#     else:
#         print("incorrect pin")

# def dispense_cash(pin, amount):
#     check(pin, amount)
#     if pin == correctpin and amount <= balance:
#         print("You're new balance is £" + str(balance - amount))

# dispense_cash(2222, 5000)

#I didn't need to make the second function... Could have written like this:

def check(pin, amount):
    if pin == correctpin and amount <= balance:
        print("dispensing cash - £" + str(amount))
        print("You're new balance is £" + str(balance - amount))
    elif balance < amount:
        print("Not enough dough in the bakery")
    else:
        print("incorrect pin")

dispense_cash(2222, 5000)