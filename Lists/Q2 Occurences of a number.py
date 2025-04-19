'''
Generate 20 random integers and store them in a list. Accept a number from the
user and print position of all occurrences of that number in the list
'''


#Solution:-
from random import random
a=[]
for i in range(21):
    a.append(int(random()*100))
print(a)
n=int(input('Enter a Number:'))
temp=0
for i in a :
    if n in a:
        print(a.index(n,temp))
        temp=a.index(n,temp)
        if n in a[temp+1:]:
            temp = a.index(n,temp+1)
        else:
            break

if n not in a:
        print('The given number is not in the random list')
