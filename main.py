import random

keywords = ["Boost", "Drain", "Amplify", "Dissipate"]

playing = False
loop_count = 0
current_position = 0
cells_collected = 0
cells_to_be_collected = 10
reactor_integrity = 3

def confirm():
    global playing, loop_count
    Confirmation = input("Gonna get the next one? (y/n) ").strip().lower()
    if Confirmation.startswith("y"):
        playing = True
        loop_count += 1
    else:
        print("Thanks for for your help!")
        loop_count = 0
        playing = False


print("\nDr. Infinity has disappeared.")
print("Without him, the reactor has become unstable.")
print("Energy cells have been scattered across the powerplant.")
print("If we don't get them back soon and stabilize the reactor, The world we know may end.")

Confirmation = input("\nWill you help us collect the energy cells? (y/n) ").strip().lower()
if Confirmation.startswith("y"):
    print("\nMay your calculations be true.")
    playing = True
else:
    print("\nWe understand the burden is too heavy.")
    playing = False

while playing == True:
    keyword = random.choice(keywords)
    starting_position = random.randint(1, 10)
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
        print("You got it!")
        cells_collected += 1
        if cells_collected == cells_to_be_collected:
            print("You've stabalized the reactor. A job well done.")
            break
        else:
            confirm()
    else:
        print(f"You missed it. The correct position was {correct_answer}") #type: ignore
        reactor_integrity -= 1
        if reactor_integrity == 0:
            print("The reactor has failed. It's over for us all.")
            break
        else:
            confirm()
    
    
