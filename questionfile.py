Questions = {
        "Regular": "\nYou are at position {position}\nThe energy cell was hit with a {keyword} {movement_int}\n\nWhere do you need to be to collect it?",
        "Unknown": "\nThe cells origin coordinates are lost (x)\nThe energy cell was hit with a {keyword} {movement_int}\n\nThe Final Position is {position}"
    }

def get_question(type: str, position: float, keyword: str, movement_int: int):
    template = Questions.get(type)
    if template:
        print(template.format(
            position=position,
            keyword=keyword,
            movement_int=movement_int
        ))
    else:
        print(f"Unknown question type: {type}")