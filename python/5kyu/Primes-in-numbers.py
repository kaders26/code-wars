# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

# my solution

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        power = 0
        while n % divisor == 0:
            power += 1
            n //= divisor
        if power > 0:
            if power == 1:
                factors.append(f"({divisor})")
            else:
                factors.append(f"({divisor}**{power})")
        divisor += 1

    return ''.join(factors)