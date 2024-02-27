# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# My solution

def sort_array(source_array):
    liste = []
    amcık = sorted([x for x in source_array if x % 2 != 0])
    for i in source_array:
        if i % 2 != 0:
            liste.append(amcık.pop(0))
        else:
            liste.append(i)
    return liste