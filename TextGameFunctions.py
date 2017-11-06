import TextGameConcept

import time
import os

kickGuyDead = False #1 is true / 0 is False

## Class for weapons
class weapons:
    #weapons followed by their respective damages
    weaponsInGame = {'bottle shank' : '5', 'knife' : '10'}
class charStats:
    health = 100
    honor = 0
    gold = 0
    inventory = []
    weaponInHand = {}


def sleep():
    return time.sleep(1)
def start():
    """Starts the beginning of the game."""
    # Acceptable moves
    moves = ['open', 'opendoor', 'openthedoor', 'walkthrough', 'continue', 'walk', 'go', 'forward']
    # Start narration
    #clearConsole()
    input('Press enter to start...')
    print("You wake up from what felt like an eternal sleep...")
    time.sleep(2)
    print("You seem to have lost all memories prior to this moment...")
    time.sleep(2)
    print("Your vision is foggy, but you make out the shape of a door")
    print("at the end of the room...")
    time.sleep(2)
    print("\nThe only thing to do is \'move forward\'")
    # Loop checks input for moves
    # Z - I changed this because it is more Pythonic, and easier to maintain because everything now falls under the same action.
    gameRunning = True
    while gameRunning == True:
        move = input('>> ')
        # Z - With these updates I had to remove the extra formatting because taking away the spaces wouldn't allow the user to move
        # Secret action in the beginning of the game. Because fuck it why not.
        if 'dunkirk' in move and 'bad' and 'sucks' in move:
            print("YOU DIED")
            gameRunning = False
        # Check to see if the user input contains an acceptable move
        elif move == 'Quit' or move == 'QUIT' or move == 'quit' or move == 'Q':
            gameRunning = False
        # Z - I changed this because it is more Pythonic, less code, simpler to read and still does what it was originally intended to do.
        elif move == 'move forward':
            c1hallway()
            return None
        else:
            print('You cannot do that..')
            time.sleep(1)
            print('Type: move forward')
def c1hallway():
    """Chapter One: First hallway after start()"""
    global inventory

    #Z- removed the action and items.

    #Print Narration
    #clearConsole()
    print("A dim light starts to fill the room as you slowly open the door...")
    time.sleep(2)
    print('You step through the door way and enter into a long stone hall way')
    print("illuminated by a series of torches mounted along the walls...")
    time.sleep(2)
    print("The hall way doesn't appear to lead anywhere, except for a small")
    print("dark hole in the wall...")
    time.sleep(2)
    # Z - We can't keep using open ended questions to continue the story.
    #print("\nWhat do you want to do?")
    print('You grab a torch off the wall and step cautiously towards the hole')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('You move the torch towards the opening')
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('A hand grabs the torch!')
    print('The wall starts to crumble before you')
    print('A noise pierces your ears')
    print('\nThe room starts to spin')
    time.sleep(1)
    print('Everything is spinning')
    time.sleep(1)
    print('Time stops')
    time.sleep(1)
    print('Your consciousness is fading')
    print('** FADE TO BLACK **')
    input('Hit enter to continue...')
    time.sleep(2)
def startScreen():
    time.sleep(3)
    print('\n' * 50)
    print('_____________________________________')
    print('      Welcome to \"TextGame\"')
    print('          A Python game')
    print('             -------')
    print('Developed by Bobby Anaya and Zac Banas')
    print('_____________________________________')
def worldIntro():
    time.sleep(1)
    print('You\'re awoken by a loud bang')
    time.sleep(1)
    print('*You hear distant voices yelling angrily')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('He can\'t stay here! They\'ll kill us all!')
    time.sleep(2)
    print('We can\'t kick him out Michael! The boy is clearly not in good health!')
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('**You think: where the fuck am I?**')
    time.sleep(1)
    print('***You try to sit up but you are still dizzy***')
    time.sleep(1)
    print('More yelling...')
    time.sleep(1)
    print('You begin to fade out of consciousness again')
    time.sleep(2)
    print('**Fade to black**')
    time.sleep(1)
    print('\n' * 10)
    print('You wake, startled, to a kick in the side')
    sleep()
    print('Get up fucker')
    sleep()
    print('*Another kick')
    sleep()
    sleep()
    print('I said get the fuck up')
def statChange(stat, IncDec, amount):
    if IncDec == 'Dec':
        print('~~your', stat, 'decreased by', amount, '~~')
    elif IncDec == 'Inc':
        print('~~your', stat, 'increased by', amount, '~~')
def statCheck(stat):
    if stat == 'health' or stat == 'Health':
        print('Your health is: ', charStats.health)
    if stat == 'honor' or stat == 'Honor':
        print('Your honor is: ', charStats.honor)
    if stat == 'inventory' or stat == 'Inventory':
        print('Your inventory contains: ', charStats.inventory)
    if stat == 'Primary Check' or stat == 'primary check':
        print('You are currently wielding a: ',charStats.weaponInHand)
    if stat == 'gold' or stat == 'Gold':
        print('You currently have: ',charStats.gold, 'gold')
def kickingGuy():
    global kickGuyDead
    userInput = input('What do you do? Fight, Run or Get up?')
    if userInput == 'Fight' or userInput == 'fight':
        print('You Granby roll into a combat base, and shoot a double leg')
        print('landing into the mount position')
        mountInput = input('Do you \'Ground and Pound\' (enter gnp), or do you slide into spiderweb and get an \'Armbar\'?')
        if mountInput == 'gnp' or mountInput == 'GNP':
            print('You start raining blows on the helpless man.')
            sleep()
            sleep()
            print('You land a brutal elbow, and see that he is unconscious')
            gnpInput = input('Do you finish the job(kill) or do you leave him be(leave)? ')
            if gnpInput == 'kill' or gnpInput == 'Kill' or gnpInput == 'KILL':
                sleep()
                print('You grab an empty bottle lying on the ground, smash it on the ground and drive the sharp edge into the man\'s throat')
                sleep()
                print('~~your honor decreased by 5~~')
                charStats.honor -= 5
                charStats.inventory.append('bottle shank')
                print('Honor: ',charStats.honor)
                sleep()
                print('You slide the glass in your front pocket')
                print('~~bottle shank added to inventory~~')
                sleep()
                sleep()
                print('You head towards the door...')
                sleep()
                kickGuyDead = True
            elif gnpInput == 'leave':
                print('You leave the man beaten and bloody, but still breathing')
                print('~~Your honor increased by 5~~')
                charStats.honor += 5
                print('Honor: ', charStats.honor)
                sleep()
                print('\nYou head towards the door...')
        elif mountInput == 'Armbar' or mountInput == 'armbar' or mountInput == 'arm bar':
            print('You fall into a snug armbar and start to push your hips in. The man cries out in pain, begging for you to stop')
            armInput = input('Do you hespect the tap(hespect) or take his arm(arm)?')
            if armInput == 'hespect' or armInput == 'Hespect' or armInput == 'respect' or armInput == 'Respect':
                print('The man rejoices, and sprints from the room...')
                sleep()
                print('You hear a door slam.. Who knows if he will return')
                sleep()
                print('You get up and dust yourself off, and make for the door...')
                charStats.honor += 5
                statChange('honor', 'Inc', 5)
            elif armInput == 'arm' or armInput == 'Arm':
                print('\nYou put his wrist under your armpit, sit back and hear his elbow snap...')
                sleep()
                print('A piercing shriek from the man.')
                sleep()
                sleep()
                print('\nAs you get up, you spit on him for good measure.')
                print('He scurries out the door crying.. Stumbling..')
                charStats.honor -= 5
                statChange('honor', 'Dec', 5)
                sleep()
                print('\nYou hear a door slam, and you smile to yourself.. Not knowing whether he will be back..')
                sleep()
                print('You head for the door...')
    elif userInput == 'Run' or userInput == 'run':
        print('You get up to your feet to run and as you run by him, he hits you hard in the back of the head')
        print('You collapse on the ground.\n')
        sleep()
        sleep()
        statChange('health','Dec', 10)
        sleep()
        print('You ask: What do you want?!')
        print('I want you to get up shit head!!')
        userInput = input('What do you do? Fight or Get up?')
        if userInput == 'Fight' or userInput == 'fight':
            print('You Granby roll into a combat base, and shoot a double leg')
            print('landing into the mount position')
            mountInput = input(
                'Do you \'Ground and Pound\' (enter gnp), or do you slide into spiderweb and get an \'Armbar\'?')
            if mountInput == 'gnp' or mountInput == 'GNP':
                print('You start raining blows on the helpless man.')
                sleep()
                sleep()
                print('You land a brutal elbow, and see that he is unconscious')
                gnpInput = input('Do you finish the job(kill) or do you leave him be(leave)? ')
                if gnpInput == 'kill' or gnpInput == 'Kill' or gnpInput == 'KILL':
                    print('You grab an empty bottle lying on the ground, smash it on the ground and drive the sharp edge into the man\'s throat')
                    print('~~your honor decreased by 5~~')
                    charStats.honor -= 5
                    charStats.inventory.append('bottle shank')
                    print('Honor: ', charStats.honor)
                    sleep()
                    print('You slide the glass in your front pocket')
                    print('~~bottle shank added to inventory~~')
                    print('You head towards the door...')
                    kickGuyDead = True
                elif gnpInput == 'leave':
                    print('You leave the man beaten and bloody, but still breathing')
                    print('~~Your honor increased by 5~~')
                    charStats.honor += 5
                    print('Honor: ', charStats.honor)
                    sleep()
                    print('\nYou head towards the door...')
            elif mountInput == 'Armbar' or mountInput == 'armbar' or mountInput == 'arm bar':
                print(
                    'You fall into a snug armbar and start to push your hips in. The man cries out in pain, begging for you to stop')
                armInput = input('Do you hespect the tap(hespect) or take his arm(arm)?')
                if armInput == 'hespect' or armInput == 'Hespect' or armInput == 'respect' or armInput == 'Respect':
                    print('The man rejoices, and sprints from the room...')
                    sleep()
                    print('You hear a door slam.. Who knows if he will return')
                    sleep()
                    print('You get up and dust yourself off, and make for the door...')
                    charStats.honor += 5
                    statChange('honor', 'Inc', 5)
                elif armInput == 'arm' or armInput == 'Arm':
                    print('\nYou put his wrist under your armpit, sit back and hear his elbow snap...')
                    sleep()
                    print('A piercing shriek from the man.')
                    sleep()
                    sleep()
                    print('\nAs you get up, you spit on him for good measure.')
                    print('He scurries out the door crying.. Stumbling..')
                    charStats.honor -= 5
                    statChange('honor', 'Dec', 5)
                    sleep()
                    print('\nYou hear a door slam, and you smile to yourself.. Not knowing whether he will be back..')
                    sleep()
                    print('You head for the door...')
        elif userInput == 'Get up' or userInput == 'get up':
            print('You wearily do as he says and get up... Sizing him up as you stand')
            sleep()
            print('The smell of whiskey from his breath permeates the room')
            sleep()
            print('He says: So what the fuck... How the fuck did you get in my goddamn.. How the fuck do--')
            sleep()
            print('MICHAEL! You leave that boy alone!')
            sleep()
            print('You shut your fuckin mouth! He\'s put us all in.. In danger!')
            print('He says to you: You stay right here you understand me?')
            sleep()
            print('The drunken man falls out of the room and you hear more yelling somewhere else in the house')
            sleep()
            print('Fuck him. You head towards the door.. Intent on finding your way out of wherever you are')
    elif userInput == 'Get up' or userInput == 'get up':
        print('You wearily do as he says and get up... Sizing him up as you stand')
        sleep()
        print('The smell of whiskey from his breath permeates the room')
        sleep()
        print('He says: So what the fuck... How the fuck did you get in my goddamn.. How the fuck do--')
        sleep()
        print('MICHAEL! You leave that boy alone!')
        sleep()
        print('You shut your fuckin mouth! He\'s put us all in.. In danger!')
        print('He says to you: You stay right here you understand me?')
        sleep()
        print('The drunken man falls out of the room and you hear more yelling somewhere else in the house')
        sleep()
        print('Fuck him. You head towards the door.. Intent on finding your way out of wherever you are')


















