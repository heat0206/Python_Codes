'''
Count how many vowels are there in a string.
Accept the string from the user.
'''

#Solution:
'''
Precondition: The code does'nt count UNIQUE
occurences of vowels.
'''

s=input("Enter string :")   
vowels=0
for ch in s:
    if ch in 'aeiouAEIOU':
        vowels+=1
       
print(vowels)
