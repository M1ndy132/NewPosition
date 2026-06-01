import random
import levels.level1 as level1, levels.level2 as level2, levels.level3 as level3, levels.level4 as level4, levels.level5 as level5, levels.level6 as level6, levels.level7 as level7, levels.level8 as level8, levels.level9 as level9, levels.level10 as level10, levels.level11 as level11, levels.level12 as level12, levels.level13 as level13, levels.level14 as level14, levels.level15 as level15, levels.level16 as level16, levels.level17 as level17, levels.level18 as level18, levels.level19 as level19, levels.level20 as level20
import questionfile as qf

levels = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10,
          level11, level12, level13, level14, level15, level16, level17, level18, level19, level20]
current_level = 0

playing = False
question_count = 0

amplify_count = 0
dissipate_count = 0

cells_collected = 0

level = levels[current_level]
cells_to_be_collected = level.cells_to_be_collected
keywords = level.keywords
reactor_integrity = level.reactor_integrity

in_play_integrity = reactor_integrity

def confirm():
    global playing
    if not next_level():
        playing = False
    else:
        Confirmation = input("Would you like to proceed to the next sector? (y/n) ").strip().lower()
        if Confirmation.startswith("n"):
            print("Rest well.")
            playing = False
        else:
            playing = True
            print(f"\n{level.section_title}")
            print(level.story_text)

def next_level():
    global current_level, playing, keywords, question_count, cells_collected, cells_to_be_collected
    global level, reactor_integrity, amplify_count, dissipate_count, Question_type, in_play_integrity

    current_level += 1
    if current_level >= len(levels):
        print("\nYou've stabalized all the sectors!")
        return False
    else:
        level = levels[current_level]
        keywords = level.keywords
        cells_to_be_collected = level.cells_to_be_collected
        reactor_integrity = level.reactor_integrity
        question_count = 0
        cells_collected = 0
        amplify_count = 0
        dissipate_count = 0
        in_play_integrity = reactor_integrity
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
    available_keywords = keywords.copy()

    if amplify_count >= 3 and "Amplify" in available_keywords:
        available_keywords.remove("Amplify")

    if dissipate_count >= 3 and "Dissipate" in available_keywords:
        available_keywords.remove("Dissipate")

    keyword = random.choice(available_keywords)

    movement_int_limited_range = [1, 2, 3, 4, 5, 10]
    
    if keyword == "Amplify":
        amplify_count += 1
        movement_int = random.choice(movement_int_limited_range)
    elif keyword == "Dissipate":
        dissipate_count += 1
        movement_int = random.choice(movement_int_limited_range)
    else:
        movement_int = random.randint(1, 10)

    Question_type = random.choice(level.Question_types)     

    if question_count < 1 and Question_type == "Regular":
        position = random.randint(1, 10)
    elif question_count < 1 and Question_type == "Unknown":
        position = random.randint(30, 60)
    else:
        position = new_position                                                      #type: ignore

    print(f"Reactor Integrity is at {in_play_integrity}/{reactor_integrity}")
    print(f"Cells collected: {cells_collected}/{cells_to_be_collected}")  

    if Question_type == "Regular":
        qf.get_question("Regular", position, keyword, movement_int)

        if keyword == "Boost":
            correct_answer = position + movement_int
        elif keyword == "Drain":
            correct_answer = position - movement_int
        elif keyword == "Amplify":
            correct_answer = position * movement_int
        elif keyword == "Dissipate":
            correct_answer = round(position/movement_int, 1)
    
    elif Question_type == "Unknown":
        qf.get_question("Unknown", position, keyword, movement_int)

        if keyword == "Boost":
            correct_answer = position - movement_int
        elif keyword == "Drain":
            correct_answer = position + movement_int
        elif keyword == "Amplify":
            correct_answer = round(position/movement_int, 1)
        elif keyword == "Dissipate":
            correct_answer = position * movement_int
    

    new_position = float(input("Position? "))


    if new_position == correct_answer:   #type: ignore
        print("\nYou got it!")
        question_count += 1
        cells_collected += 1
        if cells_collected == cells_to_be_collected:
            print("\nYou've stabalized this sector of the reactor. A job well done.")
            confirm()
    else:
        print(f"\nYou missed it. The correct position was {correct_answer}") #type: ignore
        question_count += 1
        in_play_integrity -= 1
        if in_play_integrity == 0:
            print("\nThe reactor has failed. It's over for us all.")
            playing = False
    
