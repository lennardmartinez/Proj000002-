import random
import time


# Print Delay
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Intro script
def intro(selectedmonster):
    print_pause("You find yourself standing in an open field, filled with " +
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + selectedmonster + " is somewhere " +
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)" +
                " dagger.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


# Area: Field
def area_field(stash, selectedmonster):
    # Enter 1 to knock on the door of the house/Enter 2 to peer into the cave.
    area = input("(Please enter 1 or 2.)\n")
    if area == '1':
        area_house(stash, selectedmonster)
    elif area == '2':
        area_cave(stash, selectedmonster)
    else:
        area_returnfield(stash, selectedmonster)


# Area: ReturnField
def area_returnfield(stash, selectedmonster):
    area = input("(Please enter 1 or 2.)\n")
    if area == '1':
        area_house(stash, selectedmonster)
    elif area == '2':
        area_cave(stash, selectedmonster)
    else:
        area_returnfield(stash, selectedmonster)


# Area: Cave
def area_cave(stash, selectedmonster):
    if 'magical Sword of Ogoroth' not in stash:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword " +
                    "with you.")
        print_pause("You walk back out to the field.")
        stash.append("magical Sword of Ogoroth")
        stash.remove("dagger")
        area_returnfield(stash, selectedmonster)
    elif 'magical Sword of Ogoroth' in stash:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good" +
                    " stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        area_returnfield(stash, selectedmonster)


# Area: House
def area_house(stash, selectedmonster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " +
                selectedmonster + ".")
    print_pause("Eep! This is the " + selectedmonster + "'s house!")
    print_pause("The " + selectedmonster + " attacks you!")
    area_monster(stash, selectedmonster)


# Area: Monster
def area_monster(stash, selectedmonster):
    if 'magical Sword of Ogoroth' not in stash:
        print_pause("You feel a bit under-prepared for this, what with only " +
                    "having a tiny dagger.")
    action = input("Would you like to (1) fight or (2) run away?")
    # fight
    if action == '1':
        # without weapon
        if 'magical Sword of Ogoroth' not in stash:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " +
                        selectedmonster + ".")
            print_pause("You have been defeated!")
            startover()
        # with weapon
        if 'magical Sword of Ogoroth' in stash:
            print_pause("As the " + selectedmonster + " moves to attack, " +
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand " +
                        "as you brace yourself for the attack.")
            print_pause("But the " + selectedmonster + " takes one look at " +
                        "your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + selectedmonster +
                        ". You are victorious!")
            startover()
    # runaway
    if action == '2':
        print_pause("You run back into the field. Luckily, you don't seem " +
                    "to have been followed.")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        area_returnfield(stash, selectedmonster)
    else:
        area_monster(stash, selectedmonster)


# GameEnds
def startover():
    play = input("Would you like to play again? (y/n)")
    if play == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play == 'n':
        print_pause("Thanks for playing! See you next time.")
        exit()
    else:
        startover()


# Game
def play_game():
    # monster list: Gorgon, Troll, or Dragon
    monster = ["Gorgon", "Troll", "Dragon"]
    # select a random monster from monster list
    selectedmonster = random.choice(monster)
    # create stash for hero's items
    stash = ["dagger"]
    # intro:
    intro(selectedmonster)
    area_field(stash, selectedmonster)


# Execute Game
play_game()
