'''
Calculate sin(x),x is a radian value.
(hint: use expansion of sin x)
'''

#Solution:-
x = float(input("Enter angle:"))
import math
x = x % (2.0 * math.pi)     #step needed to avoid data mishandling.
sin=0
j=0
for i in range(1,155,2):
    sin+=((-1)**j)*((x**i)/math.factorial(i))
    j+=1
print(sin)
    
