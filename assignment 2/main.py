def log_choice(text):
    """Appends the player's choices and narrative progress to adventure_log.txt."""
    with open("adventure_log.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n\n")

def start():
    # Story Beginning
    opening_text = (
        " --- Story Beginning --- \n"
        "You arrive at Ashwood Manor under the relentless downpour. The grand, looming house creaks as if it has secrets of its own.\n"
        "The count greets you with a nervous look and says he last saw his son Charlie with Jake, Charlie's best friend...\n"
        "A storm rumbles in the distance as the mystery begins.\n"
        "Do you go question Jake immediately, or search Charlie’s room for clues first?"
    )
    print(opening_text)
    log_choice(opening_text)

    while True:
        try:
            choice = int(input("Choose 1 (Question Jake) or 2 (Search Charlie’s room): ").strip())
            if choice == 1:
                narrative = "You head to Jake's room, the floorboards groaning under your boots as you prepare to interrogate him..."
                print(narrative)
                log_choice(narrative)
                narrative_two()
            elif choice == 2:
                narrative = "You decide to investigate Charlie's room, hoping his belongings will tell you more than his friend could..."
                print(narrative)
                log_choice(narrative)
                narrative_three()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_two():
    narrative = (
        "Jake seems startled when you burst in. His hands shake as he insists that the last time he saw Charlie "
        "was last night by the firepit, under the pale moonlight."
    )
    print(narrative)
    log_choice(narrative)
    print("Do you doubt Jake's story, or head to the firepit to search for clues?")
    while True:
        try:
            choice = int(input("Choose 1 (Doubt Jake) or 2 (Search the firepit): ").strip())
            if choice == 1:
                narrative = "You glare at Jake, demanding he tell the truth if he ever wants to see Charlie again..."
                print(narrative)
                log_choice(narrative)
                narrative_four()
            elif choice == 2:
                narrative = "You grab your coat and head to the firepit, the storm winds whipping around you..."
                print(narrative)
                log_choice(narrative)
                narrative_five()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_three():
    narrative = "Charlie's room smells strongly of smoke. Ash is smeared on his clothes as if he had been sitting near a fire recently..."
    print(narrative)
    log_choice(narrative)
    print("Do you question Jake about the smoke smell, or head to the fire pit to investigate?")
    while True:
        try:
            choice = int(input("Choose 1 (Question Jake) or 2 (Head to the firepit): ").strip())
            if choice == 1:
                narrative = "Fueled by suspicion, you storm down the hallway toward Jake's room..."
                print(narrative)
                log_choice(narrative)
                narrative_four()
            elif choice == 2:
                narrative = "You head to the firepit, following a faint trail of mud leading outside..."
                print(narrative)
                log_choice(narrative)
                narrative_six()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_four():
    narrative = (
        "Jake finally cracks under pressure. He confesses that Charlie left with Dee after the firepit and "
        "that they were headed toward the old bunker beneath the manor."
    )
    print(narrative)
    log_choice(narrative)
    print("Do you try to locate Dee, or head to get the keys to the bunker?")
    while True:
        try:
            choice = int(input("Choose 1 (Locate Dee) or 2 (Go get the keys): ").strip())
            if choice == 1:
                narrative = "You scour the manor looking for Dee, your footsteps echoing through the empty halls..."
                print(narrative)
                log_choice(narrative)
                narrative_eight()
            elif choice == 2:
                narrative = "You head to the dusty old study to grab the ancient, rusted bunker keys..."
                print(narrative)
                log_choice(narrative)
                narrative_nine()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_five():
    narrative = "You arrive at the firepit and spot Charlie's phone lying in the wet grass, its screen cracked but still glowing faintly..."
    print(narrative)
    log_choice(narrative)
    print("Do you try to unlock his phone, or search around the house for more clues?")
    while True:
        try:
            choice = int(input("Choose 1 (Unlock his phone) or 2 (Search house more): ").strip())
            if choice == 1:
                narrative = "You unlock his phone on the 3rd try and discover frantic texts from Dee telling him to meet her in the bunker..."
                print(narrative)
                log_choice(narrative)
                narrative_seven()
            elif choice == 2:
                narrative = "You pocket the phone and head back into the house, determined to dig deeper..."
                print(narrative)
                log_choice(narrative)
                narrative_eight()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_six():
    narrative = "You follow a faint trail of footprints in the mud leading directly toward the old bunker..."
    print(narrative)
    log_choice(narrative)
    print("Do you go to the bunker, or see if there are more clues around?")
    while True:
        try:
            choice = int(input("Choose 1 (Go to bunker) or 2 (Search for more clues): ").strip())
            if choice == 1:
                narrative = "You retrieve the bunker keys and descend the narrow stone steps into darkness..."
                print(narrative)
                log_choice(narrative)
                narrative_nine()
            elif choice == 2:
                narrative = "You sweep the surrounding grounds, flashlight cutting through the night..."
                print(narrative)
                log_choice(narrative)
                narrative_ten()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_eight():
    narrative = "While searching the house, you find a crumpled note that reads: 'Stop looking if you know what's good for you.' Moments later, you run into Dee..."
    print(narrative)
    log_choice(narrative)
    print("Do you blame Dee for the note, or ask her if she knows anything about it?")
    while True:
        try:
            choice = int(input("Choose 1 (Blame Dee) or 2 (Ask Dee): ").strip())
            if choice == 1:
                narrative = "You accuse Dee outright of writing the threatening note..."
                print(narrative)
                log_choice(narrative)
                narrative_twelve()
            elif choice == 2:
                narrative = "You calmly ask Dee if she knows who might have written such a note..."
                print(narrative)
                log_choice(narrative)
                narrative_thirteen()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_nine():
    narrative = "You descend into the bunker, the air growing colder with every step. Inside, you find a single locked door..."
    print(narrative)
    log_choice(narrative)
    print("Do you investigate the locked door, or keep searching?")
    while True:
        try:
            choice = int(input("Choose 1 (Investigate door) or 2 (Keep searching): ").strip())
            if choice == 1:
                narrative = "You press your ear to the door and hear faint movement from inside..."
                print(narrative)
                log_choice(narrative)
                narrative_eleven()
            elif choice == 2:
                narrative = "You explore the rest of the bunker, scanning for more clues..."
                print(narrative)
                log_choice(narrative)
                narrative_fourteen()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_seven():
    narrative = "The texts leave you uneasy — why would Dee lure Charlie to the bunker? Something isn't adding up..."
    print(narrative)
    log_choice(narrative)
    print("Do you head down to the bunker to look for clues, or do you go question Dee?")
    while True:
        try:
            choice = int(input("Choose 1 (Go to Bunker) or 2 (Question Dee): ").strip())
            if choice == 1:
                narrative = "You steel yourself and descend into the dark bunker..."
                print(narrative)
                log_choice(narrative)
                narrative_eleven()
            elif choice == 2:
                narrative = "You search for Dee, only to find a new note on the way accusing her of being the killer!"
                print(narrative)
                log_choice(narrative)
                narrative_twelve()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_ten():
    narrative = "You find Charlie's phone half-buried in dirt, displaying a final text from Dee telling him to meet her in the bunker..."
    print(narrative)
    log_choice(narrative)
    print("Do you head down to the bunker, or head inside to confront Dee?")
    while True:
        try:
            choice = int(input("Choose 1 or 2: ").strip())
            if choice == 1:
                narrative = "You grip the phone and descend to the bunker with determination..."
                print(narrative)
                log_choice(narrative)
                narrative_fourteen()
            elif choice == 2:
                narrative = "You storm inside, ready to confront Dee face-to-face..."
                print(narrative)
                log_choice(narrative)
                narrative_fifteen()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_twelve():
    narrative = "You accuse Dee of being behind Charlie's disappearance! She protests, saying she can prove her innocence..."
    print(narrative)
    log_choice(narrative)
    print("Do you follow Dee to the bunker, or arrest her on the spot?")
    while True:
        try:
            choice = int(input("Choose 1 (Follow Dee) or 2 (Arrest Dee): ").strip())
            if choice == 1:
                narrative = "You decide to trust Dee — for now — and follow her to the bunker..."
                print(narrative)
                log_choice(narrative)
                narrative_seventeen()
            elif choice == 2:
                narrative = "You slap the cuffs on Dee and haul her in for questioning..."
                print(narrative)
                log_choice(narrative)
                narrative_eighteen()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_thirteen():
    narrative = "Dee insists she had nothing to do with it, then suggests you question the count himself..."
    print(narrative)
    log_choice(narrative)
    print("Do you question the count, or keep looking for more clues?")
    while True:
        try:
            choice = int(input("Choose 1 (Question Count) or 2 (Look for more clues): ").strip())
            if choice == 1:
                narrative = "You march back to the count's study, suspicion written across your face..."
                print(narrative)
                log_choice(narrative)
                narrative_nineteen()
            elif choice == 2:
                narrative = "You keep searching the manor, unwilling to give up just yet..."
                print(narrative)
                log_choice(narrative)
                narrative_twenty()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_eleven():
    narrative = "You discover a hidden door in the bunker. Pressing your ear to it, you hear someone moving inside!"
    print(narrative)
    log_choice(narrative)
    print("Do you try to break the door down, or confront Dee?")
    while True:
        try:
            choice = int(input("Choose 1 (Break door down) or 2 (Confront Dee): ").strip())
            if choice == 1:
                narrative = "You brace yourself and begin breaking the door down..."
                print(narrative)
                log_choice(narrative)
                narrative_sixteen()
            elif choice == 2:
                narrative = "You leave the bunker and march toward Dee, ready for answers..."
                print(narrative)
                log_choice(narrative)
                narrative_eighteen()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_fourteen():
    narrative = "You find a note scrawled in panic — it's from Charlie, and it says Dee has taken him hostage!"
    print(narrative)
    log_choice(narrative)
    print("Do you go to Dee, or search for Charlie more?")
    while True:
        try:
            choice = int(input("Choose 1 (Go to Dee) or 2 (Search for Charlie): ").strip())
            if choice == 1:
                narrative = "You storm toward Dee, note in hand..."
                print(narrative)
                log_choice(narrative)
                narrative_eighteen()
            elif choice == 2:
                narrative = "You search every corner of the bunker until you find a locked hidden room..."
                print(narrative)
                log_choice(narrative)
                narrative_nineteen()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_fifteen():
    narrative = "You confront Dee and she seems nervous, sweat beading on her forehead..."
    print(narrative)
    log_choice(narrative)
    print("Do you arrest Dee for the disappearance of Charlie, or keep searching for clues?")
    while True:
        try:
            choice = int(input("Choose 1 (Arrest Dee) or 2 (Search for clues): ").strip())
            if choice == 1:
                narrative = "You arrest Dee on the spot..."
                print(narrative)
                log_choice(narrative)
                narrative_eighteen()
            elif choice == 2:
                narrative = "You keep investigating, refusing to jump to conclusions..."
                print(narrative)
                log_choice(narrative)
                narrative_twenty()
            else:
                print("Please choose 1 or 2 only.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def narrative_sixteen():
    narrative = (
        "After a solid 5 minutes of battering the door, it finally gives way. Inside, you find Charlie alive but frightened!\n"
        "You escort him out of the bunker, and he reveals that Dee was behind it all.\n"
        "You have successfully solved the mystery — congratulations, Detective!"
    )
    print(narrative)
    log_choice(narrative)
    exit()


def narrative_seventeen():
    narrative = (
        "Dee leads you into the bunker and points toward a hidden door, whispering that the culprit is inside.\n"
        "But as soon as you open it, you're shoved inside and locked in! You've been trapped!\n"
        "You failed to solve the mystery — you will now be Dee's next victim..."
    )
    print(narrative)
    log_choice(narrative)
    exit()


def narrative_eighteen():
    narrative = (
        "You arrest Dee and take her in for further questioning. After hours of interrogation, she finally cracks and reveals Charlie's location.\n"
        "You rescue him from the bunker and solve the case. Congratulations, Detective!"
    )
    print(narrative)
    log_choice(narrative)
    exit()


def narrative_nineteen():
    narrative = (
        "After hours of searching, you find a secret locked door. You break it down and find Charlie!\n"
        "He confirms Dee's guilt, and you bring her to justice.\n"
        "Mystery solved — well done, Detective!"
    )
    print(narrative)
    log_choice(narrative)
    exit()


def narrative_twenty():
    narrative = (
        "Despite your best efforts, no new clues turn up. The trail has gone cold...\n"
        "Charlie remains missing, and the case remains unsolved."
    )
    print(narrative)
    log_choice(narrative)
    exit()


# GAME START
choice = input(
    " Welcome to Ashwood Manor...\n"
    " You have been tasked with solving the disappearance of the count's oldest son, Charlie...\n"
    " Make decisions along the way that will either lead you closer to solving the mystery, or disappearing yourself!\n"
    " Shall we begin... (y/n): "
).strip().lower()

if choice == "y":
    # Clear previous log for a fresh game
    with open("adventure_log.txt", "w", encoding="utf-8") as f:
        f.write("Ashwood Manor Adventure Log\n")
        f.write("==========================\n\n")
    start()
else:
    print("Maybe next time...")