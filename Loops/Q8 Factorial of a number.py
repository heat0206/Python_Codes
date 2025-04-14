'''
8) Print factorial of a given number.
'''

#Solution:-
def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact



