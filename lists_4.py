#Create a function for a sub sandwich order: 5 toppings

def sub_filling(fill1, fill2, fill3, fill4, fill5):
    print("sub with {}, {}, {}, {} and {}.".format(fill1, fill2, fill3, fill4, fill5))

sub_filling("chicken", "lettuce", "tomato", "onion", "bacon")

#Create a list with 3 values and then add another to the start of the list using a method.

ma_peeps = [
    "Adam",
    "Jade",
    "Tom"
    ]

print(ma_peeps)

ma_peeps.insert(0, "Henry")

print(ma_peeps)

for peeps in ma_peeps:
    print(peeps)

for i in range(11):
    print(i)
