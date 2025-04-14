'''
3) Count no. of alphabets and no. of digits in any given string.
'''

#Solution:-
a=input("Enter a string:")

digit=0
alpha=0

for ch in a:
    if ch.isdigit():
        digit+=1
    if ch.isalpha():
        alpha+=1
        
print("The number of digits are:",digit)
print("The number of alphabets are:",alpha)

