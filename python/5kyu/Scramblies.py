# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# my solution

def scramble(s1, s2):
    s1_counts = {}
    s2_counts = {}
    
    for char in s1:
        if char.isalpha():
            char = char.lower()
            if char in s1_counts:
                s1_counts[char] += 1
            else:
                s1_counts[char] = 1
            
    for char in s2:
        if char.isalpha():
            char = char.lower()
            if char in s2_counts:
                s2_counts[char] += 1
            else:
                s2_counts[char] = 1
    
    for char, count in s2_counts.items():
        if char not in s1_counts or s1_counts[char] < count:
            return False
    
    return True