# Story start
print('You wake up in what seems to be an abandoned mineshaft.')
print('You are lying on the floor with a knife next to you.')

knife = str(input("pick it up? "))

if knife == 'yes' or knife == 'Yes':
    print('You pick up the knife and get up off the cold ground.')
    print(' ')
    knife = True
else:
    print('You decide to leave the knife and get up off the cold ground.')
    print(' ')
    knife = False

print('After getting up you see railroad tracks stretching out to a corner in front of you.')
print('Walking closer to the corner you begin to see the shadow of a figure.')

shadow = str(input('The figure is looking at you, there is no where to go behind you proceed? '))

if shadow == 'Yes' or shadow == 'yes':
    print('You head toward the shadow.')
    print(' ')
else:
    print('You have no choice but to go forward.')
    print(' ')

print('Coming closer to the man he seems to have a suit and tie.')

conceal = str(input('Put the knife in your pocket? '))

if conceal == 'yes' or conceal == 'Yes':
    print('The man greets you with a smile and puts his hand out, you shake it he begins to tell you: TBC')
    print(' ')
else:
    print('The man seems worried about the knife in your hand, he shakes his head and puts his hand out, you, surprised by this put your knife away and shake his hand, he begins to tell you: TBC')
    print(' ')

print('TBC')

# places

# weapons

# enemies

# random encounter


# inventory
hand = 'Empty'
pocket1 = 'Empty'
pocket2 = 'Empty'
holster = False
holster1 = "Not found"
holster2 = "Not found"
Backpack = False
back1 = False
back2 = False
back3 = False

# chat
sent = True
while sent == False:
    said = str(input('What next? '))
    if said == "pockets":
        print(pocket1 + " and " + pocket2 + " ")
    if said == "holsters" and holster == True:
        print(holster1 + " and " + holster2)
    if said == "holsters" and holster == False:
        print("you have no holsters")
    if said == "help":
        print("Some commands you can use are: pockets, holsters, and equipped")
    if said == "equipped":
        print(str(hand) + ' is in your hand.')
    else:
        print("That's not a command.")
