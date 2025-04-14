'''
5) Generate all Pythagorean Triplets with side length <= 30.
'''

#Solution:-
print("The pythagorian triplets with side<=30 are as follows:")
for x in range(2,31):
    for y in range(2,31):
        for z in range(2,31):
            if x**2+y**2==z**2 and x<y:
                print(x,',',y,',',z)
