import random

keywords = ["Boost", "Drain"]

playing = False
loop_count = 0
current_position = 0

def confirm():
    global playing, loop_count
    Confirmation = input("Would you like to continue playing? (y/n) ").strip().lower()
    if Confirmation.startswith("y"):
        playing = True
        loop_count += 1
    else:
        print("Thanks for playing!")
        loop_count = 0
        playing = False


Confirmation = input("Would you like to play? (y/n) ").strip().lower()
if Confirmation.startswith("y"):
    playing = True
else:
    playing = False

while playing == True:
    keyword = random.choice(keywords)
    starting_position = random.randint(1, 10)
    movement_int = random.randint(1, 10)
    

    if loop_count < 1:
        position = random.randint(1, 10)
    else:
        position = user_answer                                                      #type: ignore
        
    print(f"\nYou are at position {position}")
    print(f"The energy cell was hit with a {keyword} {movement_int}")
    print("\nWhere do you need to be to collect it?")

    user_answer = int(input("Position? "))

    if keyword == "Boost":
        correct_answer = position + movement_int
    elif keyword == "Drain":
        correct_answer = position - movement_int

    if user_answer == correct_answer:   #type: ignore
        print("You got it!")
        current_position = user_answer
        confirm()
    else:
        print(f"You missed it. The correct position was {correct_answer}") #type: ignore
        current_position = user_answer
        confirm()
    
    
