#Create an array that lists favourite films, up to 

fav_mov = [
    "star wars - revenge of the sith",
    "star wars - rogue one",
    "star wars - empire strikes back",
    "gladiator",
    "the fifth element"
]

print(fav_mov)

fav_mov.insert(4, "gangs of new york")
fav_mov.append("interstellar")

# for i in range(len(fav_mov)):
#     print(fav_mov[i])

#fav_mov.insert(2, "ghostbusters")

for film_index in fav_mov:
    print(film_index)


def film_check():
    if fav_mov[2] == "ghostbusters":
        print("yey, it's ghostbusters")
    else:
        print("boooo, we want ghostbusters")

film_check()