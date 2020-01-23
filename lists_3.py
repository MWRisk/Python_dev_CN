#Research on the following methods: remove(), reverse(),sort(), count(), extend() (and many more). 
# Create a program to demonstrate the uses of each method,some of these you may need more than one example.
# (Pay attention: not all methods would permanently updates/make changes to the lists themselves.)

Birthday_list = [
    "Adam - 1978 - 7 - 4",
    "Mum - 1948 - 10 - 20",
    "Emma - 1976 - 10 - 13",
    "Jade - 1987 - 8 - 31",
    "Sarah - 1974 - 2 - 23"
]

print(Birthday_list)

# remove()	Removes the item with the specified value

Birthday_list.remove("Adam - 1978 - 7 - 4")
# Only removes the exact "element"
print(Birthday_list)

# reverse()	Reverses the order of the list

Birthday_list.reverse()

print(Birthday_list)

Birthday_list.sort()
print(Birthday_list)


