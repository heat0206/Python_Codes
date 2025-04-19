'''
Generate 50 random numbers in the range 1 and 30.
Remove all duplicate values from the list.
'''


#Solution
import random
a=[random.randint(1,30) for i in range(50)]
print(a)
def remove_duplicate(a):
    for i in range(1,30):
        if (i in a) and  (a.count(i)>1) :
            a.remove(i)

for i in a:
    while a.count(i)>1:
        remove_duplicate(a)

a.sort()
print('new list is:\n',a)

