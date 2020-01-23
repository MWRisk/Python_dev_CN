my_riddle_text = "Forwards and backwards it reads the same. \n \nHe is called something else by others but is known to you by another name. \n"
my_riddle_answer = "dad"

def riddle(riddle_text, riddle_answer):
    print(" ")
    print (riddle_text)
    success = False
    while success == False:
        answer = input("Who is it?: ")
        if answer.lower() != riddle_answer:
            print(" ")
            print("Incorrect! Try again!")
            print(" ")
        else:
            print ("'You are correct, human!' \n \nThe dragon Swoops you up on his back, dives off the cliff and flies South West. \n \nAfter some time in flight, the dragon starts to drop altitude... 'This is as far as I wish to take you human' \n \n He sets you down.)
            success = True

riddle(my_riddle_text, my_riddle_answer)



