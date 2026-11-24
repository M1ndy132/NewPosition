from tkinter import *
from story import run_story, list_of_saves

def run_story_save(win, save_name):
    if save_name == "New Session":
        run_story(win)
    else:
        run_story(win, save_name)

def main(win, mode):
    if mode == "Story":
        info_lbl_1 = Label(win)
        info_lbl_2 = Label(win)

        if list_of_saves:
            info_lbl_1.config(text="Marker detected.")
            info_lbl_2.config(text="Here's a list of saved markers\nPress the marker you wish to teleport to:")

            info_lbl_1.pack()
            info_lbl_2.pack()

            Button_list = []
            for n in range(len(list_of_saves)):
                for item in list_of_saves[n]:
                    item_button = Button(win, text=f"{item}, Level: {list_of_saves[n][item]["level"]}", command=lambda item=item: run_story_save(win, item))
                    Button_list.append(item_button)

            for button in Button_list:
                 button.pack()

            new_session_btn = Button(win, text="New Session", command=lambda: run_story_save(win, "New Session"))
            new_session_btn.pack()

        else:
            run_story(win)
    else:
        info_lbl_3 = Label(win, text="Unknown Mode")
        info_lbl_3.pack()
