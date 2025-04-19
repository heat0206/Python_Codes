'''
Create a list of 5 odd integers using random nos.
Similarly create a list of 4 even integers using random nos.
Replace the third element of odd integers with a list of 4 even integers.
Flattern,sort and print the list. Provide appropriate message at each stage.
'''

#Solution:
import random

lst1=random.sample(range(1,100,2),5)
lst2=random.sample(range(2,100,2),5)

print('Odd no. List:',lst1)
print('Even no. list:',lst2)


lst1[2]=lst2    #Replacing 3rd element
print('\n3rd element of odd number list replaced')
print('now the list is:\n',lst1)

print("\nFlatterned list is :\n") #Flatterning    
lst1.pop(2)
a=0
for i in range(2,2+len(lst2)):
    lst1.insert(i,lst2[a])
    a+=1
print(lst1)

lst1.sort()    #Sort the list
print('\nSorted the list')
print('Sorted list:\n',lst1)
