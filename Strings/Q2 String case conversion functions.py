'''
Write your own functions (without using built-in functions) to convert all
characters of a string into lower case/upper case/toggle case.
'''

#Solution:-

def convert_U_to_L(a):
    result=''
    for ch in a:
        ch=chr(ord(ch)+32)
        result+=ch
    return result

def convert_L_to_U(a):
    result=''
    for ch in a:
        ch=chr(ord(ch)-32)
        result+=ch
    return result

def convert_toggle(a):
    result=''
    for ch in a:
        if 'a'<=ch<='z':
            ch=chr(ord(ch)-32)
            result+=ch

        elif 'A'<=ch<='Z':
            ch=chr(ord(ch)+32)
            result+=ch
    return result 


