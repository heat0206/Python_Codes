'''
Generate 30 random numbers and put them in a list.
Create two more lists –one containing only +ve numbers and another with –ve nos.
'''

#Solution
import random
a=[random.randint(-50,50) for i in range(30)]
b,c=[],[]
print('original list:',a,'\n')
for i in a :
    if i>=0:
        b.append(i)
    if i<0:
        c.append(i)

print('Positive numbers list:',b,'\n')
print('Negative numbers list:',c,'\n')
