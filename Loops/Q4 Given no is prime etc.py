'''
4) Check whether a given number is prime, is perfect, is Armstrong,
   is palindrome, is automorphic.
'''

##Solution:-

a=int(input("Enter a number:"))
#Prime:
flag=0
for i in range(3,a):
    if a%i == 0:
        flag+=1
if flag==1:
    print('Not Prime')
elif flag!=1 or a==2:
    print('Prime')
    

#Palindrome:
a=str(a)
if a==a[len(a)::-1]:
    print("Pallindrome")
else:
    print("NOT a Pallindrome")

#Perfect Number:
a=int(a)
total=0
for d in range(1,a):
    if a%d==0:
        total+=d
if total==a:
    print("Perfect Number")
else:
    print("NOT a Perfect Number")

#Armstrong Number:
a=str(a)
temp=0
digits=len(a)
for i in a:
    i=int(i)
    temp+=(i**digits)

a=int(a)
if temp==a:
    print("Armstrong Number")
else:
    print("NOT a Armstrong Number")

#Automorphic Number:
sqr=a**2
sqr=str(sqr)
temp=sqr[len(sqr)-digits:len(sqr)]
temp=int(temp)
if temp==a:
    print("Automorphic Number")
else:
    print("Not Automorphic")

    


