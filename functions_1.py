#Lets go back to our noughts and crosses board Write an if statement that checks if the items
#on the top row meet a winning condition. So the top row are all ‘o’s or all ‘x’s

space1 = 'X'
space2 = 'X'
space3 = 'X'
space4 = 'X'
space5 = 'X'
space6 = ' '
space7 = 'O'
space8 = ' '
space9 = ' '
print('   |   |   ')
print(' {} | {} | {} '.format(space1,space2,space3))
print('   |   |   ')
print('-----------')
print('   |   |   ')
print(' {} | {} | {} '.format(space4,space5,space6))
print('   |   |   ')
print('-----------')
print('   |   |   ')
print(' {} | {} | {} '.format(space7,space8,space9))
print('   |   |   ')

#top line winning
if space1 == space2 == space3:
    print("winner")
else:
    print("\n")
