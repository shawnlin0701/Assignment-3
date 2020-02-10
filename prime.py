"""
prime.py -- Write the application code here
"""
def generate_prime_factors(Number):
    #setting the variables and list
    count = 0
    prime_factors = []
    dividend = Number

    #for loop to check for prime factors and append them to a list
    for i in range(2, (Number//2+1)):
        while dividend % i == 0:
            prime_factors.append(i)
            dividend = dividend//i
            count = count + 1
            i = 2

    # returning the result and the list of prime factors
    if count == 0 and Number != 1:
        print(" %d is a Prime Number" %Number)
    else:
        print(" %d is not a Prime Number" %Number)
        print(prime_factors)
