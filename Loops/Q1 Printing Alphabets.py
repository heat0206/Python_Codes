'''
1) Print all alphabets in upper case and in lower case.
'''

#Solution:-
print('Alphabets in Lower Case:')
for i in range(97,123):
    print(chr(i),end=' ')

print('\nAlphabets in Upper Case:')
for i in range(65,91):
    print(chr(i),end=' ')
