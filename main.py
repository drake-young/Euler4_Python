# ===========================================================
# PROBLEM 4 -- Largest palindrome product
# ===========================================================
#
# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two
# 3-digit numbers
#
# ===========================================================
from timeit    import default_timer
from functools import reduce
from math      import sqrt

# ===========================================================
# FUNCTION: get_largest_prime_factor
# ===========================================================
#
#  Input: integer n to find the largest prime factor of
#
#  Output: the largest prime number that divides n
#
#  Task:    iterate through integers <= sqrt(n), checking if
#           that integer divides n. this continues until all
#           integers that divide n have been accounted for,
#           and returns that integer
#
# ===========================================================
def get_largest_prime_factor( n ):
    i        =  2
    largest  =  0

    # Check integers between 2 and sqrt(n)
    while i * i <= n:

        # If the current integer divides n, divide n (factor i out)
        if n % i is 0:
            n      //=  i
            largest  =  i

        # If the integer does not divide n, then increment and continue
        else:
            i  +=  1

    # Return the largest factor (or n if n was prime)
    return max( largest , n )


# ===========================================================
# FUNCTION: getFactors
# ===========================================================
#
#  Input: integer n to find the factors of
#
#  Output: set containing all integers that divide n
#
#  Task:    generate a list of all integers that divide n,
#           reduce the list using functools.reduce, and
#           return this reduced list as a set.
#
# ===========================================================
def get_factors( n ):
    return set(  # Cast to set to ensure uniqueness
            reduce(  # Reduce to perform "list.__add__" (add item to list) from the passed generator
                list.__add__,
                ( [ i , n//i ]
                    for i in range( 1 , int( sqrt(n) + 1 ) )  # check all positive integers <= sqrt(n)
                    if n % i is 0 ) ) )  # only add if i is a factor of n


def problem_4( ):
    # Print the Problem Context
    print( "Project Euler Problem 4 -- Largest Palindrome Product" )

    # Set Up Variables
    start_time  =  default_timer( )  # start timer
    product     =  999 * 999         # maximum possible product
    repeat      =  True              # true if loop should iterate again
    result      =  0                 # store the answer

    # Primary Loop, iterate through the numbers and check
    while  product > 100 * 100 and repeat:
        product_string    =  str( product )
        product_reversed  =  product_string[ : : -1 ]

        # Check if number is palindrome
        if product_string == product_reversed:
            # Check if number is not prime
            if get_largest_prime_factor( product ) != product:
                # Check all possible factors for a pair of 3-digit numbers
                factors  =  get_factors( product )
                for x in factors:
                    # Verify that both factors contain 3 digits
                    if len( str(x) ) is 3 and len( str( product//x ) ) is 3:
                        result  =  product
                        repeat  =  False
                        break
        product  -=  1

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Largest Palindrome made from the product of two 3-digit numbers:   %d"      %  result )
    print( "   Computation Time:                                                  %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_4( )
