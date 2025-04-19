'''
Take two lists of numbers.
Create third list of numbers for only those numbers from first list which are
not there in 2nd list (use list comprehension).
'''


#Solution :
from random import random
lst1=[int(random()*10)for i in range(5)]
lst2=[int(random()*10)for i in range(5)]

print('lst1:',lst1)
print('lst2:',lst2)

lst3=[lst1[i]for i in range(len(lst1)) if lst1[i] not in lst2 ]
print('lst3:',lst3)
