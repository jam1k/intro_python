# Write your solution here
from unittest import result


def reading_file(filename):
    lines = ''.join(list(open(filename)))
    parts = lines.split("\n\n")
    result = {}

    for part in parts:
        data = part.split("\n")
        key = data[0]
        value = data[1:]
        result[key] = value

    return result

def search_by_name(filename: str, word: str):
    receipes = reading_file(filename)
    result = []
    for receipe in receipes:
        if word in receipe.lower():
            result.append(receipe)
    return result

def search_by_time(filename: str, prep_time: int):
    receipes = reading_file(filename)
    result = []
    name_time = {}

    for receipe_name, time in receipes.items():
        name_time[receipe_name] = int(time[0])

    for name, time in name_time.items():
        if time <= prep_time:
            result.append(f"{name}, preparation time {time} min")
    return result

def search_by_ingredient(filename: str, ingredient: str):
    receipes = reading_file(filename)
    result = []
    
    for key, value in receipes.items():
        time  = value[0]
        ingredients = value[1:]
        if ingredient in ingredients:
            result.append(f"{key}, preparation time {time} min")
    return result
