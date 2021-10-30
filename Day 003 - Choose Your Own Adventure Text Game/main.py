'''
Day 3 of the 100 days of code python challenge - The objective of this project is to make a text based adventure 
using control flow so that users can make choices and arrive at different endings with one ending to be to find
buried treasure
'''
import time
import re
import sys

#initialise game over ascii art
game_over = '''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
'''

#initialise good ending ascii art
game_clear = '''
                                               888            
                                               888            
                                               888            
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                             888                              
                        Y8b d88P                              
                         "Y88P"                          

'''


#print some fun ascii art to start the adventure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')

#variable time breaks
a = 1.5

#Occasional wait clauses for effect
time.sleep(a)
#print the introduction
print('Welcome to Treasure Island.')
time.sleep(a)
print('Your missions is to find the Treasure')
time.sleep(a)
print('|The Back Story|')
time.sleep(a)
print('Your name is Jackson Gray, an adventurer and treasure hunter')
time.sleep(a)
print('You recently got wind of a famous Pirate\'s buried treasure.')
time.sleep(a)
print('You have followed the clues to the Island De La Muerta, a small Island with a population of about 500')
print('')
time.sleep(a)


#The first section of the game - choice 1
print('You land on the Island that has been indicated in the treasure map')
print('')
time.sleep(a)

#regex helps to get multiple matches
jungle = re.compile('[Jj]ungle')
check_map = re.compile('[Cc]heck *[Mm]ap')
#Use a while loop to keep circling until an appropriate answer is given
while True:
    print('Do you take some time to check the map? Or venture straight into the jungle - I mean you\'re a pro who needs a map!')
    print('')
    #get user input
    choice_1 = input('Jungle? Check Map? ')
    print('')
    time.sleep(a)
    #if elif else block which checks if the answer maps to either of the choices or loops back round if not
    if jungle.match(choice_1):
        choice_1 = 'J'
        map_checked = False
        print('')
        break
    elif check_map.match(choice_1):
        choice_1 = 'CM'
        map_checked = True
        print('')
        break
    else:
        print('Please give a valid input, answer either "Jungle" or "Check Map"')
        print('')
        time.sleep(a)

#Choice 1 decided - move to consequence of choice
if choice_1 == 'CM':
    print('You notice at the bottom of the map there is the faint outline of some words')
    time.sleep(a)
    print('Some of the letters are illegible but you can still make out some of what it says')
    time.sleep(a)
    print('The message reads:')
    time.sleep(a)
    print('My na-- be S---lm-n, This map lea-- to me buri--- Tr--s-re')
    time.sleep(a)
    print('You feel this might be important later.')
    time.sleep(a)
    print('You take some time to check the map and confirm your route before heading into the jungle')
    print('')
    time.sleep(a)

#Back to converge point
print('You come to a cross roads with a left and right path')
time.sleep(a)
if map_checked:
    print('You seem to remember the correct path is right')
    time.sleep(a)
print('')

#initialise regex variables for the choice_2
left = re.compile('[Ll]eft')
right = re.compile('[Rr]ight')

#while block to handle input for the second choice
while True:
    print('which path do you take?')
    time.sleep(a)
    print('')
    choice_2 = input('Left? Right? ')
    print('')
    time.sleep(a)
    if left.match(choice_2):
        choice_2 = 'L'
        break
    elif right.match(choice_2):
        choice_2 = 'R'
        break
    else:
        print('Please give a valid input, "Left" or "Right"')
        time.sleep(a)
        print('')

#If choice 2 was bad end run this if block
if choice_2 == 'L':
    print('You walk down the path for a while, but suddenly you lose your footing and slip, falling into a pit.')
    time.sleep(a)
    print('At the bottom of the pit, you notice the remains of dead travellers to your left and right')
    time.sleep(a)
    print('You have accidentally fallen into the Lion\'s den...')
    time.sleep(a)
    print('You hear a roar from above and suddenly a pack of lions jump down appearing in front of you.')
    time.sleep(a)
    print('It doesn\'t look like there\'s any way out... and well, you know what happens next.')
    time.sleep(a)
    print('')
    print('')
    print('BAD END - GAME OVER - PLAY AGAIN TO TRY AND FIND THE TRUE TREASURE')
    time.sleep(a)
    print('')
    print(game_over)
    time.sleep(30)
    sys.exit()

#initialise money variable as it will be important later
money = 20

#Move to the next section of the Story
print('You head down the path on the right and come to a small town.')
time.sleep(a)
print('This island is bigger than you expected.')
time.sleep(a)
print('You decide to go to the local bar to stop for a drink')
print('')
time.sleep(a)

#setup for choice 3
print('You sit down at the bar, and a haggard, drunken, smelly old man comes up beside you')
time.sleep(a)
print('The man asks if you could please buy him a drink')
time.sleep(a)
print('You only have 20 coins, drinks cost 5 each and you\'re already buying one for yourself')
print('')
time.sleep(a)

#initialise regex patterns
yes = re.compile('[Yy](es|ES)?')
no = re.compile('[Nn](o|O)?')

#while block to capture valid input
while True:
    print('Will you buy the man a drink as well?')
    print('')
    time.sleep(a)
    choice_3 = input('Yes? No? ')
    print('')
    time.sleep(a)
    if yes.match(choice_3):
        choice_3 = 'Y'
        money -= 10
        break
    elif no.match(choice_3):
        choice_3 = 'N'
        money -= 5
        break
    else:
        print('Please give a valid input. Type either "Y" or "N" or "Yes" or "No"')
        print('')
        time.sleep(a)

#handle consequence of choice_3
if choice_3 == 'Y':
    print(f'You buy both yourself and the man a drink, leaving only {money} coins left for yourself')
    time.sleep(a)
    print('The man thanks you and then pulls you in close to whisper in your ear')
    time.sleep(a)
    print('"Meet me by the old well at midnight, I have some information to give you in return for your kindness" The man says')
    print('')
    time.sleep(a)
elif choice_3 == 'N':
    print(f'You buy just yourself a drink, leaving {money} coins left')
    time.sleep(a)
    print('The man grumbles some curses about you under his breath before drunkenly stumbling out of the bar')
    print('')
    time.sleep(a)

#enter setup for choice_4
print('You decide to stay at the inn for the night as you\'re wary and tired after travelling')
time.sleep(a)
print('The bartender offers you a deal, he says he\'ll let you stay at the inn for free, but only if you tell him what you\'re doing in town')
time.sleep(a)
print('If you don\'t, he\'ll charge you the full room price of 5 coins for the night')

#while block until valid input
while True:
    print('Do you trust the man enough to tell him why you\'re there? You could use the free night\'s sleep')
    print('')
    time.sleep(a)
    choice_4 = input('Yes? No? ')
    print('')
    if yes.match(choice_4):
        choice_4 = 'Y'
        barkeeper = True
        break
    elif no.match(choice_4):
        choice_4 = 'N'
        money -= 5
        barkeeper = False
        break
    else:
        print('Please give a valid input. Type either "Y" or "N" or "Yes" or "No"')
        print('')
        time.sleep(a)

if choice_4 == 'Y':
    print('You tell the barkeeper about the reason you\'re there, and the secret treasure of the legendary dead pirate')
    time.sleep(a)
    print('The barkeeper listens intently and closely, smiling as you regail the story')
    time.sleep(a)
    print('You finish your story and the barkeeper thanks you, assuring you that you\'re stay in the inn that night will be free')
    print('')
    time.sleep(a)
elif choice_4 == 'N':
    print('The man scowls a little. "I guess you\'re the secretive type huh')
    time.sleep(a)
    print('He seems visibly offended')
    time.sleep(a)
    print('"Well your secrets will cost you 5 gold coins for the night" he says sharply')
    time.sleep(a)
    print('You hand over the money and head up to your room, feeling it not a good idea to stick around in the bar much longer')
    print('')
    time.sleep(a)

#handling the further consequences of choice_3 if the player bought the man a drink
if choice_3 == 'Y':
    print('At midnight you head out to the old well to meet the drunken man from before')
    time.sleep(a)
    print('When you arrive he is no longer drunk and speaks perfectly well')
    time.sleep(a)
    print('"I was in disguise before, I had to know what sort of person you were before I gave you this info" he says')
    time.sleep(a)
    print('"I know why you\'re here... you\'re looking for the legendary pirate\'s buried treasure aren\'t you"')
    time.sleep(a)
    print('You look shocked, you\'re not sure if you can trust this man or not.')
    time.sleep(a)
    print('')
    print('"Oh don\'t worry, I have no interest in such pointless things" the man chuckles')
    time.sleep(a)
    print('"But if you do, you\'ll have to know how to solve the ancient riddle of the gatekeeper"')
    time.sleep(a)
    print('"The gatekeeper will ask you for the secret password, and the answer is the legendary pirate\'s name!"')
    time.sleep(a)
    print('"Don\'t get too excited though, the pirate was very private and only his closest crewmates knew his name"')
    time.sleep(a)
    print('"Any records of it have been lost by now, but maybe you\'ll figure something out"')
    time.sleep(a)
    print('You think on the mans words before thanking him and heading back to the inn to get some sleep.')
    print('')
    time.sleep(a)

#Setting up the next scene
print('You wake up after a good night\'s sleep at the inn feeling refreshed and ready to venture back into the jungle')
time.sleep(a)
print('You wade into the jungle until you come to a river crossing, the river is very wide, but you think you could swim across')
time.sleep(a)
print('A sign says that there is a boat that will come to take travellers across for free')
time.sleep(a)
print('You worry that if you wait too long for the boat you\'ll have to sleep in the dangerous jungle later')
print('')
time.sleep(a)

#set up for choice_5 - initializing regex

swim = re.compile('[Ss]wim *([Aa]cross)?')
wait = re.compile('[Ww]ait')

#initialise player_health variable
player_health = 100

#while block to capture valid input
while True:
    print('Do you try to swim across? Or wait for the boat?')
    print('')
    time.sleep(a)
    choice_5 = input('Wait? Swim Across? ')
    print('')
    time.sleep(a)
    if wait.match(choice_5):
        choice_5 = 'W'
        waited = True
        break
    elif swim.match(choice_5):
        choice_5 = 'SA'
        player_health -= 20
        waited = False
        break
    else:
        print('Please give valid input, type either "Wait" or "Swim Across"')
        print('')
        time.sleep(a)

#handle the consequences of choice 5
if choice_5 == 'SA':
    print('As you\'re swimming across you get attacked by a crocodile!')
    time.sleep(a)
    print('This isn\'t your first rodeo and you manage to fight it off, but it deals a nasty bite to your arm.')
    time.sleep(a)
    print('You lose 20 health, you only have {player_health} points remaining')
    print('')
    time.sleep(a)
elif choice_5 == 'W':
    print('You feel it\'s safer to wait for the boat, who knows what\'s in the water.')
    time.sleep(a)
    print('You wait for what feels like forever, but sure enough after 3 hours, a boat appears to ferry you across')
    print('')
    time.sleep(a)

print('You arrive on the other side of the river')
time.sleep(a)
#prints a different message based on the truthiness of the waited variable
print('You thank the boatman for his kindness'*(waited) + 'You treat the wound on your arm to stop the bleeding, and wait 10 minutes to dry out'*(not waited))
time.sleep(a)
print('When you\'re ready, you head further into the jungle')
print('')
time.sleep(a)

#setup next scene
print('You continue along your path and come to a large wall blocking your path')
time.sleep(a)
print('on the wall is a riddle, at the top reads a warning')
time.sleep(a)
print('Solve this puzzle to pass, but beware, those who fail it more than once will meet a terrible doom')
time.sleep(a)
print('Just as you are about to read the puzzle, a mysterious man emerges from the jungle')
time.sleep(a)
print('"I know the answer to that riddle, and I\'ll tell you for 10 coins" The man says')
print('')
time.sleep(a)

#an if block to check if you have enough money anyway
if money < 10:
    puzzle_solve = True
    print(f'You tell the man you only have {money} coins left')
    time.sleep(a)
    print('He laughs at you calling you poor and then skulks back into the jungle leaving you to solve the puzzle yourself.')
    print('')
    time.sleep(a)
    choice_6 = ''
else:
    #While block to catch valid input
    while True:
        print('Do you pay the man to solve the puzzle for you?')
        print('')
        time.sleep(a)
        choice_6 = input('Yes? No? ')
        print('')
        time.sleep(a)
        if yes.match(choice_6):
            choice_6 = 'Y'
            puzzle_solve = False
            money -= 10
            break
        elif no.match(choice_6):
            choice_6 = 'N'
            puzzle_solve = True
            break
        else:
            print('Please give a valid input. Type either "Y" or "N" or "Yes" or "No"')
            print('')
            time.sleep(a)

#handle consequence of choice 6
if choice_6 == 'N':
    print('The mysterious man laughs at you as if to be amused by your stupidity before disappearing into the jungle')
elif choice_6 == 'Y':
    print('The man solves the puzzle for you swiftly and disappears into the forest')

#Setup the puzzle
#set up answer match
answer = re.compile('([Tt]he)? *[Gg]erman *([Mm]an)?')

#initialise attempt counter
attempts = 0

#If puzzle_solve variable is true then jump into the puzzle
if puzzle_solve == True:
    print('You realise you\'ll have to solve the puzzle so you take you\'re time to read through it')
    time.sleep(a)
    print('The puzzle reads as follows')
    print('')
    time.sleep(a)

    #explain the concept
    print('|The Situation|')
    time.sleep(a)
    print('1. There are 5 houses in 5 different colours.')
    time.sleep(a)
    print('2. In each house, lives a person with a different nationality')
    time.sleep(a)
    print('3.These 5 owners drink a certain type of beverage, smoke a certain brand of cigar, and keep a certain pet')
    time.sleep(a)
    print('4. No owners have the same pet, smoke the same brand of cigar or drink the same beverage')
    time.sleep(a)
    print('The question is, who owns the fish?')
    print('')
    time.sleep(a)

    #give the hints
    print('Here are your hints')
    time.sleep(a)
    print('|The Hints|')
    time.sleep(a)
    print('- The Brit lives in the red house')
    time.sleep(a)
    print('- The Swede keeps dogs as pets')
    time.sleep(a)
    print('- The Dane drinks tea')
    time.sleep(a)
    print('- The green house is on the left of the white house')
    time.sleep(a)
    print('- The green house\'s owner drinks coffee')
    time.sleep(a)
    print('- The person who smokes Pall Mall rears birds')
    time.sleep(a)
    print('- The owner of the yellow house smokes Dunhill')
    time.sleep(a)
    print('- The man living in the centre house drinks milk')
    time.sleep(a)
    print('- The Norwegian lives in the first house')
    time.sleep(a)
    print('- The man who smokes blends lives next to the man who keeps cats')
    time.sleep(a)
    print('- The man who keeps horses lives next to the man who smokes Dunhill')
    time.sleep(a)
    print('- The owner who smokes BlueMaster drinks beer')
    time.sleep(a)
    print('- The German smokes Prince')
    time.sleep(a)
    print('- The Norwegian lives next to the blue house')
    time.sleep(a)
    print('- The man who smokes blend has a neighbour who drinks water')
    print('')
    time.sleep(a)

    print('Take your time with this to work it out, you can only try twice')
    time.sleep(a)
    print('You finish reading and decide to attempt the puzzle')
    print('')
    time.sleep(a)

    #get answer using while block
    while True:
        print('Who has the fish?')
        print('')
        time.sleep(a)
        player_answer = input('Please give your answer in the following form: "The Brit", "The Norwegian", "The Dane" etc. ')
        print("")
        time.sleep(a)
        #check if right answer, if not increase attempts count
        if answer.match(player_answer):
            break
        else:
            attempts += 1
        #if attempts count is too high, give a game over
        if attempts > 1:
            print('The loud ominous voice booms')
            time.sleep(a)
            print('"MWUHAHAHAHA, YOU DANCED WITH THE DEVIL TWICE AND LOST, I\'LL BE TAKING YOUR SOUL BACK TO THE UNDERWORLD WITH ME"')
            time.sleep(a)
            print('An extremely bright light begins to glow from the wall with increasing intensity')
            time.sleep(a)
            print('The bright light engulfs you, turning you to ash as your soul is ripped down to the underworld')
            print('')
            time.sleep(a)
            print('BAD END - GAME OVER - PLAY AGAIN TO TRY AND FIND THE TRUE TREASURE')
            print('')
            time.sleep(a)
            print(game_over)
            time.sleep(30)
            sys.exit()
        else:
            print('A loud ominous voice booms from an unknown source')
            time.sleep(a)
            print('MWUHAHAHAHA DON\'T GET IT WRONG AGAIN OR THERE\'LL BE TROUBLE')
            time.sleep(a)


#move to the post puzzle sequence
print('As the puzzle is solved and the answer has been said you feel the ground shaking underneath you')
time.sleep(a)
print('The wall where the puzzle was once written crumbles away, revealing a passage to a tomb.')
print('')
time.sleep(a)

#is waited true? if so move to sleeping the night scene
if waited == True:
    print('It\'s beginning to get late and you\'re too tired to explore right now')
    time.sleep(a)
    print('You decide instead to set up camp in the jungle for the night and explore the tomb tomorrow')
    print('')
    time.sleep(a)

    #enter jungle_sleep_choice section
    print("In the night you hear some creepy sounds, almost like screams or laughs coming from the jungle")
    print('')
    time.sleep(a)

    #Get jungle sleep choice, use while block to capture valid input
    while True:
        print('Do you go and check out the source of the sound?')
        print('')
        time.sleep(a)
        jungle_sleep_choice = input('Yes? No? ')
        print('')
        time.sleep(a)
        if yes.match(jungle_sleep_choice):
            jungle_sleep_choice = 'Y'
            break
        elif no.match(jungle_sleep_choice):
            jungle_sleep_choice = 'N'
            player_health -= 20
            break
        else:
            print('Please give a valid input. Type either "Y" or "N" or "Yes" or "No"')
            print('')
            time.sleep(a)
    
    #handle consequences of jungle_sleep_choice
    if jungle_sleep_choice == 'Y':
        print('You investigate the source of the sound and find that it\'s a pack of sleeping hyaenas!')
        time.sleep(a)
        print('Good job you got the jump on them before they got the jump on you!')
        time.sleep(a)
        print('You light your fire torch and quickly chase them away before getting back to sleep')
        print('')
        time.sleep(a)
    elif jungle_sleep_choice == 'N':
        print('You decide not to go and check it out, judging that it is probable something you don\'t want to find')
        time.sleep(a)
        print('However it turns out the source of the sound was a sleeping pack of hyaenas!')
        time.sleep(a)
        print('They wake up and attack you whilst you\'re sleeping')
        time.sleep(a)
        print('You manage to fight them off but sustain some injuries. You lose 20 health')
        time.sleep(a)
        print(f'You have {player_health} health left.')
        print('')
        time.sleep(a)

#move into the tomb scene, print about waking up if you slept the night
print('You wake up feeling refreshed\n\n'*(waited) + 'You enter the tomb ready to to uncover the secret treasure')
print('')
time.sleep(a)

#time for choice_7
print('As you\'re walking through the tomb you come to a door which has a left switch and a right switch')
print('')
time.sleep(a)

#time to handle choice_7
#while block to capture valid input
while True:
    print('Do you press the left switch or the right switch?')
    print('')
    time.sleep(a)
    choice_7 = input('Left? Right? ')
    print('')
    if right.match(choice_7):
        choice_7 = 'R'
        break
    elif left.match(choice_7):
        choice_7 = 'L'
        player_health -= 35
        break
    else:
        print('Please give a valid input, "Right" or "Left"')
        print('')
        time.sleep(a)

#handle consequences of choice_7
if choice_7 == 'L':
    print('As you press the button you hear an ominous laugh bellow throughout the tomb')
    time.sleep(a)
    print('"HAHAHAHA WRONG ANSWER" the mysterious voice says')
    time.sleep(a)
    print('A trap is triggered and arrows fire from the wall, One pierces your shoulder')
    time.sleep(a)
    print('You\'ll survive but you\'re hurt, you lose 35 health')
    time.sleep(a)
    print(f'You have {player_health} health remaining')
    time.sleep(a)
    print('You treat the wound and press the right switch')
    print('')
    time.sleep(a)

#handle next scene
print('The door opens for you and you walk through to a new passage with murals and paintings all over the walls')
time.sleep(a)
print('You see some writing on the wall that says "Here lie the remains of -kul--a-" the last word has faded slightly')
print('')
time.sleep(a)

#if map_checked is true then have revelation
if map_checked:
    print('As you read the letters you feel like you\'ve seen something similar before')
    time.sleep(a)
    print('Hang on a minute, you have! The name in the writing at the bottom of your map! You pull out your map and put 2+2 together')
    time.sleep(a)
    print('THE WORD IS SKULLMAN')
    time.sleep(a)
    print('This must be the legendary pirates name')
    time.sleep(a)
    print('You take careful note of it before moving on')
    print('')
    time.sleep(a)
else:
    print('You feel this might be important but you can\'t figure out what it means so you move on')
    print('')
    time.sleep(a)


#handle what happens if barkeeper variable is true then
if barkeeper:
    print('As you progress through the tomb you suddenly hear a loud voice from behind you')
    time.sleep(a)
    print('"STOP RIGHT THERE!" it\'s the barkeeper from before and he has two men with him')
    time.sleep(a)
    print('"Sorry to do this to you Jackson, but we\'ll be taking it from here, the treasure is ours... nothing personal, just business" he says')
    time.sleep(a)
    print('Guess he wasn\'t so trustworthy, you curse yourself for telling him why you were here')
    time.sleep(a)
    print('There\'s no choice, you\ll have to fight them off, but do you still have the strenth to do it after everything you\'ve been through')
    print('')
    time.sleep(a)

    #if statement to check if you have enough health to win
    if player_health < 50:
        print('You fight your hardest but after everything you\'ve been through')
        time.sleep(a)
        print('You\'re too weary and injured to win')
        time.sleep(a)
        print('The men overpower you and you meet your untimely demise at their hands')
        print('')
        time.sleep(a)
        print('BAD END - GAME OVER - PLAY AGAIN TO TRY AND FIND THE TRUE TREASURE')
        print('')
        time.sleep(a)
        print(game_over)
        time.sleep(30)
        sys.exit()
    else:
        print("it's a difficult fight but we can't forget that you're a pro!")
        time.sleep(a)
        print('You take on all 3 men and give them the fight of their lives')
        time.sleep(a)
        print('They run away whilst they can, injured badly and terrified of what you\'ll do if they stay')

#The final choices
print('You continue through the tomb and finally come to the final chamber')
time.sleep(a)
print('There you lay your eyes upon a room full of treasure the likes of which you\'ve never seen')
time.sleep(a)
print('You walk further in but then out of nowhere the ghost of the legendary dead pirate appears to block your path')
time.sleep(a)
print('')
print('"AHAHAHAHAHAHAHA YOU WHO VENTURES INTO MY TOMB, I HOPE YOU\'VE MADE THE RIGHT CHOICES"')
time.sleep(a)
print('"IT\'S TIME FOR THE FINAL RIDDLE TO PROVE YOU ARE WORTHY OF MY TREASURE"')
time.sleep(a)
print('"GET IT RIGHT AND I WILL GIVE YOU MY TREASURE, BUT GET IT WRONG AND I\'LL TAKE YOUR SOUL BACK TO THE UNDERWORLD WITH ME"')
time.sleep(a)
print('"SO WILL YA PLAY THE GAME?"')
print('')
time.sleep(a)

#This is actually the most important choice even thought it doesn't feel like it
while True:
    print("Will you play the riddle?")
    print('')
    time.sleep(a)
    important_choice = input("Yes? No? ")
    print('')
    time.sleep(a)
    if yes.match(important_choice):
        important_choice = 'Y'
        break
    elif no.match(important_choice):
        important_choice = 'N'
        break
    else:
        print('Please give a valid input. Type either "Y" or "N" or "Yes" or "No"')
        print('')
        time.sleep(a)

#time for the secret correct ending
if important_choice == 'N':
    print('You think for a moment, and then decide that no amount of treasure is worth such an obvious risk to your life')
    time.sleep(a)
    print('You politely decline the ghost, who looks totally bewildered, and decide to head home')
    time.sleep(a)
    print('You retire from treasure hunting, and settle down into a normal life')
    time.sleep(a)
    print('You meet a nice girl, settle down and start a family')
    time.sleep(a)
    print('You realise there is more to life than the riches and adventure you always chased up to this point')
    time.sleep(a)
    print('The real treasure has been waiting right here all along')
    time.sleep(a)
    print('You live a long and fulfilled life - and on your death bed you are surrounded by those close to you')
    time.sleep(a)
    print('You pass on into the next life with no regrets')
    print('')
    time.sleep(a)
    print('WELL DONE - YOU FOUND THE GOOD ENDING - THANKS FOR PLAYING')
    print('')
    time.sleep(a)
    print(game_clear)
    time.sleep(30)
    sys.exit()

#initialise final answer pattern
final_answer = re.compile('[Ss][Kk][Uu][Ll][Mm][Aa][Nn]')

#final choice
print('"HAHAHAHAHAHAHA" The ghosts voice booms')
time.sleep(a)
print('"HERE IS YOUR FINAL RIDDLE - HAVE YOU BEEN PAYING ATTENTION TO THE CLUES?')
print('')
time.sleep(a)

print('"WHAT IS THE SECRET PASSWORD!?"')
print('')
time.sleep(a)

#get answer
secret_pass = input('Enter your answer: ')
print('')
time.sleep(a)

if final_answer.match(secret_pass):
    print('The ghosts smile fades and he looks slightly annoyed.')
    time.sleep(a)
    print('"Ugh, fine... I guess you can just take it" he mumbles apathetically before disappearing into dust.')
    time.sleep(a)
    print('You take the treasure back home thinking that you have finally made it')
    time.sleep(a)
    print('But the riches change your life in a way you didn\'t expect')
    time.sleep(a)
    print('The people close to you turn to leeches who are only after your money')
    time.sleep(a)
    print('You find it impossible to form real bonds with those around you as they are only using you for your money')
    time.sleep(a)
    print('You spend your life in the lap of luxury, but the whole time intensley lonely')
    time.sleep(a)
    print('You long for someone to truly share your life with, but never find them')
    time.sleep(a)
    print('On your death bed you look back over your life')
    time.sleep(a)
    print('You wonder what might have been if you\'d have never taken that stupid ghosts challenge and answered his final riddle')
    time.sleep(a)
    print('If you\'d have left the treasure and looked for something more fulfilling, would it have been better?')
    time.sleep(a)
    print('You pass onto the next life full of regrets and loneliness')
    time.sleep(a)
    print('Is this the dead pirate\'s final curse? his final riddle? the riddle he didn\'t even know he was asking?')
    time.sleep(a)
    print('In your final moments you\'re reminded of an old shanty your grandfather used to sing to you as a kid')
    print('')
    time.sleep(a)

    print('Beware, beware of the wealth of treasure')
    time.sleep(3)
    print('You\'ll fight for your life in search of that pleasure')
    time.sleep(3)
    print('But once you bite gold there\'s no going back')
    time.sleep(3)
    print('You\'ll live with that curse till you\'re swallowed into the black.')
    print('')
    time.sleep(3)

    print('BAD END - WAIT WHAT? BUT YOU GOT THE TREASURE RIGHT? THIS DOESN\'T MAKE SENSE!')
    time.sleep(a)
    print('MAYBE THERE WAS MORE TO THAT CHOICE TO DO THE RIDDLE THAN YOU THOUGHT')
    print('')
    time.sleep(a)

    print(game_over)
    time.sleep(30)
    sys.exit

else:
    print('"MWUHAHAHAH WRONG ANSWER, I\LL BE TAKING THAT SOUL OF YOURS!"')
    print('')
    time.sleep(a)
    print('BAD END - GAME OVER - PLAY AGAIN TO TRY AND FIND THE TRUE TREASURE')
    print('')
    time.sleep(a)
    print(game_over)
    time.sleep(30)
    sys.exit()