#remove a string from an already existing one
def remove_string():
    st=input("Enter a string:")
    r=input("Enter string to be removed:")
    if r in st:
        new=st.replace(r,'')
        return new
    else:
        return "string not present in given string"

print(remove_string())



    
