"""
prime.py -- Write the application code here
"""
def generate_prime_factors(Number):
    count = 0
    intergers = []
    dividend = Number
    for i in range(2, (Number//2+1)):
        while dividend % i == 0:
            intergers.append(i)
            dividend = dividend//i
            count = count + 1
            i = 2

    if count == 0 and Number != 1:
        print(" %d is a Prime Number" %Number)
    else:
        print(" %d is not a Prime Number" %Number)
        print(intergers)
