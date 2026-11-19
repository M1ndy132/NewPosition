from tkinter import *
from story import run_story, list_of_saves






def start(game_win):
    
    title_lbl = Label(game_win, text="Reactor Math") 
    info_lbl = Label(game_win, text="")
    info_lbl2 = Label(game_win, text="")

    title_lbl.pack()
    info_lbl.pack()
    info_lbl2.pack()

    def story():
        if list_of_saves:
            info_lbl.config(text="Marker detected.\nHere's a list of saved markers")
            save = Entry(game_win)
            save.pack()
            
            for n in range(len(list_of_saves)):
                dict1 = list_of_saves[n]
                for item in dict1:
                    info_lbl2.config(text=f"{item}, Level: {dict1[item]["level"]} ")
            save_name = save.get()
            if save_name == "n":
                run_story(game_win)
            else:
                run_story(game_win, save_name)

    story_btn = Button(game_win, text="Story Mode", command=story)
    quit_btn = Button(game_win, text="Quit", command=exit)

    story_btn.pack()
    quit_btn.pack()


    """while option := input("Select a mode. ").strip().lower():
        match option:
            case "story":
                if list_of_saves:
                    print("Marker detected.")
                    print("here's a list of saved markers")
                    for n in range(len(list_of_saves)):
                        dict1 = list_of_saves[n]
                        for item in dict1:
                            print(f"{item}, Level: {dict1[item]["level"]} ")
                    save = input("Would you like to teleport to saved marker? Enter name or 'n' ").strip().title()
                    if save == "n":
                        run_story()
                    else:
                        run_story(save)
                else:
                    run_story()
            case _:
                break"""

