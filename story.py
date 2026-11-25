from tkinter import *
import random
import json
import levels.level1 as level1, levels.level2 as level2, levels.level3 as level3, levels.level4 as level4, levels.level5 as level5, levels.level6 as level6, levels.level7 as level7, levels.level8 as level8, levels.level9 as level9, levels.level10 as level10, levels.level11 as level11, levels.level12 as level12, levels.level13 as level13, levels.level14 as level14, levels.level15 as level15, levels.level16 as level16, levels.level17 as level17, levels.level18 as level18, levels.level19 as level19, levels.level20 as level20
import questionfile as qf

levels = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10,
          level11, level12, level13, level14, level15, level16, level17, level18, level19, level20]

SAVE_FILE = "saves.json"

def load_saves():
    try:
        with open(SAVE_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_progress(win):
    info_lbl_1 = Label(win, text="Markers tell us where we left off.")
    user_confirm_lbl = Label(win, text="Would you like to make a marker?")
    button_frame = Frame(win)

    info_lbl_1.pack()
    user_confirm_lbl.pack()
    button_frame.pack()

    user_confirm_yes_btn = Button(button_frame, text="Yes", command=lambda: user_save_confirm(win, info_lbl_1, "Yes"))
    user_confirm_no_btn = Button(button_frame, text="No", command=lambda: user_save_confirm(win, info_lbl_1, "No"))

    user_confirm_yes_btn.grid(row=0, column=0)
    user_confirm_no_btn.grid(row=0, column=1)

def user_save_confirm(win, label, confirmation):
    if confirmation == "Yes":
        save_name_label = Label(win, text="Name the marker: ")
        save_name_entry = Entry(win)

        save_name_label.pack()
        save_name_entry.pack()
        name = save_name_entry.get()
        level = current_level

        new_save = {
            name: {
                "level": level
            } 
        }

        list_of_saves.append(new_save)

        with open(SAVE_FILE, "w") as f:
            json.dump(list_of_saves, f, indent=2)
    else:
        label.config(text="The time machine's seeing some use.")

def load_progress(save_name=None):
    try:
        with open(SAVE_FILE) as file:
            data = json.load(file)
    except FileNotFoundError:
        return 0

    if save_name is None:
        return 0

    for save in data:
        if save_name in save:
            return save[save_name]["level"]

    return 0


current_level = load_progress()

playing = False
question_count = 0

amplify_count = 0
dissipate_count = 0

cells_collected = 0

current_level_data = levels[current_level]
cells_to_be_collected = current_level_data.cells_to_be_collected
keywords = current_level_data.keywords
reactor_integrity = current_level_data.reactor_integrity

in_play_integrity = reactor_integrity

game_state = {
    "position": 0,
    "question count": question_count
}


list_of_saves = load_saves()

def next_level_confirm(win):
    global playing
    if not next_level(win):
        ...
        # Exit
    else:
        confirmation_lbl = Label(win, text="Would you like to proceed to the next sector?")
        confirm_yes_btn = Button(win, text="Yes", command=lambda: begin_next_level_confirm(win, confirmation_lbl, "Yes"))
        confirm_no_btn = Button(win, text="No", command=lambda: begin_next_level_confirm(win, confirmation_lbl, "No"))


def begin_next_level_confirm(win, label, confirmation):
    if confirmation == "No":
        label.config(text="Rest well. We can continue a next time. Let's put a marker on the map.")
        save_progress(win)
    else:
        win.after(1000, lambda: next_level(win))
        
def begin_confirm(win, label, confirmation):
    if confirmation == "Yes":
        label.config(text="May your calculations be true.")
        game_loop(win)
    else:
        label.config(text="We understand the burden is too heavy.")
        

def next_level(win):
    global current_level, current_level_data, playing, keywords, question_count, cells_collected, cells_to_be_collected
    global level, reactor_integrity, amplify_count, dissipate_count, Question_type, in_play_integrity

    for widgit in win.winfo_children():
        widgit.destroy()

    info_lbl_1 = Label(win)
    section_title_lbl = Label(win)
    story_text_lbl = Label(win)

    current_level += 1
    if current_level >= len(levels):
        info_lbl_1.config(text="You've stabalized all the sectors!")
        info_lbl_1.pack()
        #exit
    else:
        current_level_data = levels[current_level]
        keywords = current_level_data.keywords
        cells_to_be_collected = current_level_data.cells_to_be_collected
        reactor_integrity = current_level_data.reactor_integrity
        game_state["question count"] = 0
        cells_collected = 0
        amplify_count = 0
        dissipate_count = 0
        in_play_integrity = reactor_integrity
        section_title_lbl.config(text=f"{current_level_data.section_title}")
        story_text_lbl.config(text=current_level_data.story_text)

        section_title_lbl.pack()
        story_text_lbl.pack()
        win.after(1000, lambda: game_loop(win))

def display_current_stats(win):
    global in_play_integrity, reactor_integrity, cells_collected, cells_to_be_collected

    reactor_int_lbl = Label(win, text=f"Reactor Integrity is at {in_play_integrity}/{reactor_integrity}")
    cells_col_lbl = Label(win, text=f"Cells collected: {cells_collected}/{cells_to_be_collected}")

    reactor_int_lbl.pack()
    cells_col_lbl.pack()

def questions(win, question_type, position, keyword, movement_int):
    question_frame = Frame(win)
    question_lbl = Label(question_frame)

    answer_list = []

    for widgit in win.winfo_children():
        if isinstance(widgit, Button):
            widgit.destroy()

    button_frame = Frame(question_frame)

    answer_1_btn = Button(button_frame)
    answer_2_btn = Button(button_frame)
    answer_3_btn = Button(button_frame)

    # get question
    if question_type == "Regular":
        question_lbl.config(text=qf.get_question("Regular", position, keyword, movement_int))

        correct_answer, alt_answer_1, alt_answer_2 = answers("Regular", position, movement_int, keyword)
        answer_list.extend([correct_answer, alt_answer_1, alt_answer_2])
        """(f"Testing: {correct_answer, alt_answer_1, alt_answer_2}")"""

    
    elif question_type == "Unknown":
        question_lbl.config(text=qf.get_question("Unknown", position, keyword, movement_int))

        correct_answer, alt_answer_1, alt_answer_2 = answers("Unknown", position, movement_int, keyword)
        answer_list.extend([correct_answer, alt_answer_1, alt_answer_2])
        """print(f"Testing: {correct_answer, alt_answer_1, alt_answer_2}") """

    random.shuffle(answer_list)

    question_frame.pack()
    question_lbl.pack()

    button_frame.pack()

    answer_1_btn.config(text=answer_list[0], command=lambda: check_answer(win, answer_list[0], question_type, position, keyword, movement_int))
    answer_2_btn.config(text=answer_list[1], command=lambda: check_answer(win, answer_list[1], question_type, position, keyword, movement_int))
    answer_3_btn.config(text=answer_list[2], command=lambda: check_answer(win, answer_list[2], question_type, position, keyword, movement_int))



    answer_1_btn.grid(row=0, column=0)
    answer_2_btn.grid(row=0, column=1)
    answer_3_btn.grid(row=0, column=2)
    

def answers(qtype, position, movement_int, keyword):
    if qtype == "Regular":
        keyword_master_list = [{"Key": "Boost", "Calculation": (position + movement_int)}, 
                           {"Key": "Drain", "Calculation": (position - movement_int)}, 
                           {"Key": "Amplify", "Calculation": (position * movement_int)}, 
                           {"Key": "Dissipate", "Calculation": round(position/movement_int, 1)}]
    elif qtype == "Unknown":
        keyword_master_list = [{"Key": "Boost", "Calculation": (position - movement_int)}, 
                                   {"Key": "Drain", "Calculation": (position + movement_int)}, 
                                   {"Key": "Amplify", "Calculation": round(position/movement_int, 1)}, 
                                   {"Key": "Dissipate", "Calculation":position * movement_int}]

    for key in keyword_master_list:
            if keyword == key["Key"]:
                correct_answer = key["Calculation"]

    wrong_keywords = [key for key in keyword_master_list if key["Key"] != keyword and key["Calculation"] != correct_answer] 

    
    alt_answer_1_keyword, alt_answer_2_keyword = random.sample(wrong_keywords, 2) 
    alt_answer_1 = alt_answer_1_keyword["Calculation"]
    alt_answer_2 = alt_answer_2_keyword["Calculation"]


    return correct_answer, alt_answer_1, alt_answer_2

def check_answer(win, answer, question_type, position, keyword, movement_int):
    global question_count, cells_collected, in_play_integrity
    new_position = answer
    correct_answer = answers(question_type, float(position), float(movement_int), keyword)[0]

    for widgit in win.winfo_children():
            if isinstance(widgit, Frame):
                widgit.destroy()

    ans_check_frame = Frame(win)
    message_lbl_1 = Label(ans_check_frame)
    message_lbl_2 = Label(ans_check_frame)

    ans_check_frame.pack()


    if new_position == correct_answer:   #type: ignore
        message_lbl_1.config(text="You got it!")
        message_lbl_1.pack() 
        game_state["question count"] += 1
        cells_collected += 1
        game_state["position"] = answer
             
        
        if cells_collected == cells_to_be_collected:
            message_lbl_2.config(text="You've stabalized this sector of the reactor. A job well done.")
            win.after(1200, lambda: next_level_confirm(win))
            message_lbl_2.pack()
        else:
            win.after(1200, lambda: next_question(win))
        
        
    else:
        message_lbl_1.config(text=f"You missed it. The correct position was {correct_answer}") #type: ignore
        game_state["question count"] += 1
        in_play_integrity -= 1
        game_state["position"] = answer
        message_lbl_1.pack()

        if in_play_integrity == 0:
            message_lbl_2.config(text="The reactor has failed. It's over for us all.")
            message_lbl_2.pack()
        else:
            win.after(1200, lambda: next_question(win))



    

def next_question(win):
    for widgit in win.winfo_children():
        widgit.destroy()

    game_loop(win)


def run_story(win, save_name=None):
    global playing, current_level, current_level_data
    global cells_to_be_collected, keywords, reactor_integrity
    global amplify_count, dissipate_count, question_count, in_play_integrity, cells_collected

    resumed = False
    if save_name:
        current_level = load_progress(save_name)
        current_level_data = levels[current_level]
        cells_to_be_collected = current_level_data.cells_to_be_collected
        keywords = current_level_data.keywords
        reactor_integrity = current_level_data.reactor_integrity
        in_play_integrity = reactor_integrity
        game_state["question count"] = 0
        cells_collected = 0
        amplify_count = 0
        dissipate_count = 0
        resumed = True

    for widgit in win.winfo_children():
        widgit.destroy()

    section_title_lbl = Label(win, text=current_level_data.section_title)
    story_text_lbl = Label(win, text=current_level_data.story_text)
    

    section_title_lbl.pack()
    story_text_lbl.pack()

    if not resumed:
        info_lbl = Label(win, text="Will you help us collect the energy cells?")
        
        begin_yes_btn = Button(win, text="Yes", command=lambda: begin_confirm(win, info_lbl, "Yes"))
        begin_no_btn = Button(win, text="No", command=lambda: begin_confirm(win, info_lbl, "No"))

        info_lbl.pack()
        begin_yes_btn.pack()
        begin_no_btn.pack()  
    else:
        game_loop(win)

def game_loop(win):
        global playing, current_level, current_level_data
        global cells_to_be_collected, keywords, reactor_integrity
        global amplify_count, dissipate_count, question_count, in_play_integrity, cells_collected
        
        available_keywords = keywords.copy()

        if current_level_data.cells_to_be_collected <= 15:
            if amplify_count >= 3 and "Amplify" in available_keywords:
                available_keywords.remove("Amplify")

            if dissipate_count >= 3 and "Dissipate" in available_keywords:
                available_keywords.remove("Dissipate")
        else:
            if amplify_count >= 6 and "Amplify" in available_keywords:
                available_keywords.remove("Amplify")

            if dissipate_count >= 6 and "Dissipate" in available_keywords:
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

        Question_type = random.choice(current_level_data.Question_types)     

        if game_state["question count"] == 0:
            if Question_type == "Regular":
                game_state["position"] = random.randint(1, 10)
            elif Question_type == "Unknown":
                game_state["position"] = random.randint(30, 60)
                                                     
        display_current_stats(win)

        questions(win, Question_type, game_state["position"], keyword, movement_int)
        
    
