'''
7) Print nCr and nPr.
'''

#Solution:-
from my_functions import factorial
n=int(input("Enter n:"))
r=int(input("Enter r:"))

c= factorial(n)/(factorial(r)*factorial(n-r))

p= factorial(n)/factorial(n-r)

print("nCr =",c)
print("nPr =",p)




