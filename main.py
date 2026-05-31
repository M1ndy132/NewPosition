import random

keywords = ["Boost", "Drain"]

playing = False

def confirm():
    global playing
    Confirmation = input("Would you like to continue playing? (y/n) ").strip().lower()
    if Confirmation.startswith("y"):
        playing = True
    else:
        print("Thanks for playing!")
        playing = False


Confirmation = input("Would you like to play? (y/n) ").strip().lower()
if Confirmation.startswith("y"):
    playing = True
else:
    playing = False

while playing == True:
    keyword = random.choice(keywords)
    position = random.randint(1, 10)
    movement_int = random.randint(1, 10)

    print(f"You are at position {position}")
    print(f"The energy cell was hit with a {keyword} {movement_int}")
    print("Where do you need to be to collect it?")

    user_answer = int(input("Position? "))

    if keyword == "Boost":
        correct_answer = position + movement_int
    elif keyword == "Drain":
        correct_answer = position - movement_int

    if user_answer == correct_answer:   #type: ignore
        print("You got it!")
        confirm()
    else:
        print(f"You missed it. The correct position was {correct_answer}") #type: ignore
        confirm()

    
