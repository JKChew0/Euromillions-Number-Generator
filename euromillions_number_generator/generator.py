import random

import stats

""" 
Get a number that is either odd or even, and either low or high, add the number to a list a certain number of times.
Use flags to count how many odd or even numbers there are
Repeat code for number of times chosen.

Step 1 - get a an odd or even number. 
Step 2 - determine if it's high or low
Step 3 - add high or low number to ticket list and increment a counter. 
Step 4 - repeat until there's enough high/low, and odd/even.

Get a number
If odd and high - add to list and decrement odd and high
elif odd and low - add to list and decrement odd and low
elif even and high - add to list and decrement even and high
elif even and low - add to list and decrement even and low
Repeat until odd, even, high, and low have enough
"""

def euromillions_number_generator():
    """A number generator for the euromillions."""
    ticket = []
    stars = []

    stats.odd = int(input("How many odd numbers would you like?"))
    stats.even = int(input("How many even numbers would you like?"))
    stats.high = int(input("How many high numbers would you like?"))
    stats.low = int(input("How many low numbers would you like?"))
    stats.stars = 2

    n = 0

    while stats.odd > 0:
        add_number(stats, ticket)
    while stats.even > 0:
        add_number(stats, ticket)
    while stats.high > 0:
        add_number(stats, ticket)
    while stats.low > 0:
        add_number(stats, ticket)
    while stats.stars >0:
        get_luck_stars(stats, stars)

    ticket.sort()
    stars.sort()

    print("Ticket: " + str(ticket) + "\nLucky stars: " + str(stars))

def get_luck_stars(stats, stars):
    """Create a list of 2 unique random numbers between 1 and 12. """
    n = random.randint(1, 12)
    if n not in stars:
        stars.append(n)
        stats.stars -= 1
    else:
        pass
    return stars

def get_number():
    """Create a random number between 1 and 50 and return it to be used."""
    n = random.randint(1, 50)
    return n

def check_high_low(n):
    """Return True if it is in the range 1-25."""
    if n in range(1, 26):
        return False
    else:
        return True

def check_odd_even(n):
    """Return True if even."""
    if n % 2:
        # Odd
        return True
    else:
        # Even
        return False

def add_number(stats, ticket):
    n = get_number()
    if check_odd_even(n) and check_high_low(n):
        if stats.odd > 0 and stats.high > 0:
            if n not in ticket:
                ticket.append(n)
                stats.odd -= 1
                stats.high -= 1
            else:
                pass
        else:
            pass
    elif check_odd_even(n) and not check_high_low(n):
        if stats.odd > 0 and stats.low > 0:
            if n not in ticket:
                ticket.append(n)
                stats.odd -= 1
                stats.low -= 1
            else:
                pass
        else:
            pass
    elif not check_odd_even(n) and check_high_low(n):
        if stats.even > 0 and stats.high > 0:
            if n not in ticket:
                ticket.append(n)
                stats.even -= 1
                stats.high -= 1
            else:
                pass
        else:
            pass
    elif not check_odd_even(n) and not check_high_low(n):
        if stats.even > 0 and stats.low > 0:
            if n not in ticket:
                ticket.append(n)
                stats.even -= 1
                stats.low -= 1
            else:
                pass
        else:
            pass
    print("Odd: " + str(stats.odd) + "\nEven: " + str(stats.even) + "\nHigh: " + str(stats.high) + "\nLow: " + str(stats.low))

euromillions_number_generator()
