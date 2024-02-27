# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

# My solution
def persistence(n):
    if n < 10:
        return 0
    else:
        say = 0
        while len(str(n)) != 1:
            n_sayi = str(n)
            new_n = [int(digit) for digit in n_sayi]
            sonuc = 1
            for i in new_n:
                sonuc *= i
            n = sonuc
            say += 1
        return say