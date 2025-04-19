# Menu-Driven Stack
lst=[]
while 1:
    print("\nStack Operations:\n1)Push element\n2)Pop element\n3)Exit")
    a=int(input("Enter number:"))
    
    if a == 1:
        inpt=input("Enter element to be added:")
        if inpt.isdigit():
            lst.append(int(inpt))
        else:
            lst.append(inpt)
        print("Element added to list\nList is:\n",lst)

    if a == 2:
        inpt=input("Enter element to pop:")
        if inpt.isdigit():
            if int(inpt) in lst:
                lst.remove(int(inpt))
                print("pop successful!\nList now is:\n",lst)
            else:
                print("Element not present in list")
        elif inpt.isalpha():
            if inpt in lst:
                lst.remove(inpt)
                print("pop successful!\nList now is:\n",lst)
            else:
                print("Element not present in list")
        

    if a == 3:
        break
        
