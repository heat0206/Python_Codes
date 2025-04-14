'''
2) Print a multiplication table of a given number.
'''

#Solution :-

a= int(input("Enter a number :"))
for i in range(1,11):
    print(a,"x",i,"=",a*i)
