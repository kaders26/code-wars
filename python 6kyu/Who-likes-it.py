# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# My solution

def likes(names):
    if isinstance(names, str):
        kelimeler = names.split(" ")
    elif isinstance(names, list):
        kelimeler = names
    else:
        raise ValueError("Input must be a string or a list.")

    kelimelers = len(kelimeler)
    if kelimelers == 0:
        return "no one likes this"
    elif kelimelers == 1:
        return f"{kelimeler[0]} likes this"
    elif kelimelers == 2:
        return f"{kelimeler[0]} and {kelimeler[1]} like this"
    elif kelimelers == 3:
        return f"{kelimeler[0]}, {kelimeler[1]} and {kelimeler[2]} like this"
    else:
        return f"{kelimeler[0]}, {kelimeler[1]} and {kelimelers - 2} others like this"