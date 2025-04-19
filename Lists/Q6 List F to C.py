'''
Convert list of temperatures in Fahrenheit degrees to
equivalent Celsius degrees.
'''

#Solution:
import random
def F_to_C(f):
    c=5/9*(f-32)
    return c

t=0
a=[random.randint(-50,50)for i in range(10)]
print('Farenheit temp:',a)
for i in a :
    a[t]=F_to_C(i)
    t+=1

print('Celcius temp:',a)

    

