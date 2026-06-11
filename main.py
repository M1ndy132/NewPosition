import json
from story import run_story, list_of_saves



while option := input("Select a mode. ").strip().lower():
    match option:
        case "story":
            if list_of_saves:
                print("Marker detected.")
                print("here's a list of saved markers")
                for n in range(len(list_of_saves)):
                    dict1 = list_of_saves[n]
                    for item in list_of_saves[n]:
                        print(f"{item}, Level: {list_of_saves[n][item]["level"]} ")
                save = input("Would you like to teleport to saved marker? Enter name or 'n' ").strip().lower()
                if save == "n":
                    run_story()
                else:
                    run_story(save)
            else:
                run_story()
        case _:
            break