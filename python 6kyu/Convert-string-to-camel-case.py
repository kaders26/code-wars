# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

# My solution

def to_camel_case(text):
    if not text:
        return ""

    words = text.replace("-", " ").replace("_", " ").split()
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]

    return ''.join(camel_case_words)