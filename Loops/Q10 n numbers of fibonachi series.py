'''
10) Generate N numbers of Fibonacci series.
'''

#Solution :-
n=int(input("Enter N:"))
terms=0
a=0
b=1
while terms<n:
    print(a)
    c=a+b
    a=b
    b=c
    terms+=1

        
