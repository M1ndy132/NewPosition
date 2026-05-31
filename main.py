import random
import level1, level2

levels = [level1, level2]
current_level = 0

playing = False
loop_count = 0


cells_collected = 0

level = levels[current_level]
cells_to_be_collected = level.cells_to_be_collected
keywords = level.keywords

reactor_integrity = 3

def confirm():
    global playing, loop_count
    if not next_level():
        playing = False
    else:
        Confirmation = input("Would you like to proceed to the next sector? (y/n) ").strip().lower()
        if Confirmation.startswith("n"):
            print("Rest well.")
            playing = False
        else:
            playing = True
            print(level.section_title)
            print(level.story_text)

def next_level():
    global current_level, playing, keywords, loop_count, cells_collected, cells_to_be_collected, level, reactor_integrity
    current_level += 1
    if current_level >= len(levels):
        print("\nYou've stabalized all the sectors!")
        return False
    else:
        level = levels[current_level]
        keywords = level.keywords
        cells_to_be_collected = level.cells_to_be_collected
        loop_count = 0
        cells_collected = 0
        reactor_integrity = 3
        return True


print(level.section_title)
print(level.story_text)

Confirmation = input("\nWill you help us collect the energy cells? (y/n) ").strip().lower()
if Confirmation.startswith("y"):
    print("\nMay your calculations be true.")
    playing = True
else:
    print("\nWe understand the burden is too heavy.")
    playing = False

while playing == True:
    keyword = random.choice(keywords)
    movement_int = random.randint(1, 10)
    

    if loop_count < 1:
        position = random.randint(1, 10)
    else:
        position = user_answer                                                      #type: ignore

    print(f"Reactor Integrity is at {reactor_integrity}/3")
    print(f"Cells collected: {cells_collected}/{cells_to_be_collected}")    
    
    print(f"\nYou are at position {position}")
    print(f"The energy cell was hit with a {keyword} {movement_int}")
    print("\nWhere do you need to be to collect it?")

    user_answer = float(input("Position? "))

    if keyword == "Boost":
        correct_answer = position + movement_int
    elif keyword == "Drain":
        correct_answer = position - movement_int
    elif keyword == "Amplify":
        correct_answer = position * movement_int
    elif keyword == "Dissipate":
        correct_answer = round(position/movement_int, 1)

    if user_answer == correct_answer:   #type: ignore
        print("\nYou got it!")
        loop_count += 1
        cells_collected += 1
        if cells_collected == cells_to_be_collected:
            print("\nYou've stabalized this sector of the reactor. A job well done.")
            confirm()
    else:
        print(f"\nYou missed it. The correct position was {correct_answer}") #type: ignore
        loop_count += 1
        reactor_integrity -= 1
        if reactor_integrity == 0:
            print("\nThe reactor has failed. It's over for us all.")
            playing = False
    
