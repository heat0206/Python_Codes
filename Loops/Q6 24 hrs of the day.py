'''
6) Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
'''


#Solution:-

for i in range(24):
    if i==0 :
        suffix = "midnight"
    elif i==12:
        suffix = "noon"
    elif 0<i<12:
        suffix = 'AM'
    elif 12<i<24:
        suffix = 'PM'
    print(i,suffix)
