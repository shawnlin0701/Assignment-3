"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    #setting the variables and list
    prime_factors = []
    dividend = int(number)
    #check for speacial cases
    if number == 1:
        print(prime_factors)
        return prime_factors

    if number == 2:
        prime_factors.append(number)
        print(prime_factors)
        return prime_factors

    if number == 3:
        prime_factors.append(number)
        print(prime_factors)
        return prime_factors

    #for loop to check for prime factors and append them to a list
    for i in range(2, number//2+1):
        while dividend % i == 0:
            prime_factors.append(i)
            dividend = dividend//i
        else:
            i = 2
    # returning the list of prime factors
    print(prime_factors)
    return prime_factors
