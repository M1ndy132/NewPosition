from tkinter import *
from main import main


win = Tk()
win.config(width=500, height=400)
win.pack_propagate(False)
win.resizable(False, False)
win.title("Game")
win.eval('tk::PlaceWindow . center')

bg_image = PhotoImage(file='floating islands.png')
bg_label = Label(win, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def start_game(mode):
    win.destroy()
    
    game_win = Tk()
    game_win.config(width=500, height=400)
    game_win.pack_propagate(False)
    game_win.resizable(False, False)
    game_win.title("Reactor")

    main(game_win, mode)





    

menubar = Menu(win)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Start Story Mode", command=lambda: start_game("Story"))
file_menu.add_command(label="Restart Game")

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="How to Play")
help_menu.add_command(label="Rules")
help_menu.add_command(label="Controls")

about_us_menu = Menu(menubar, tearoff=0)
about_us_menu.add_command(label="History")
about_us_menu.add_command(label="Who We Are")

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)
menubar.add_cascade(label="About Us", menu=about_us_menu)

title_lbl = Label(win, text="New Position")
title_lbl.pack()

story_btn = Button(win, text="Story", command=lambda: start_game("Story"))
story_btn.pack()

win.config(menu = menubar)


    

win.mainloop()
