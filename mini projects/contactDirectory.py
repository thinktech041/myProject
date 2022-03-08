import sys

def InitPhonebookState():
    rows, coloms = int(input("PLEASE INPUT THE INITIAL NUMBER OF CONTACTS:")),5
    Phone_Book= []
    print(Phone_Book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" %(i+1))
        print("NOTE: * Denotes Mandatory Files")
        print("......................................................................")
        temp=[]
        empty=['',' ']
        for j in range(coloms):
            if j==0:
                temp.append(str(input("Enter name*: ")))
                
                if temp[j] in empty:
                    sys.exit("Name is Mandatory. Exiting due to blank field..")
            elif j==1:
                temp.append(int(input("Enter number*: ")))

            elif j==2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] in empty:
                    temp[j]= None
            elif j==3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] in empty:
                    temp[j]=None
            elif j==4:
                temp.append(str(input("Enter Category(Family/Friend/Work/Others): ")))
                if temp[j] in empty:
                    temp[j]=None

        phone_book.append(temp)
    print(Phone_Book)
    return Phone_Book


def Menu():
    print("###########################################################")
    print("\t\t\tPHONE DIRECTORY", flush=False)
    print("###########################################################")
    print("\tYou can now perform the following operations on this Phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a  contact")
    print("5. Show all contacts")
    print("6. Exit Phonebook")
    choice = int(input("Please enter your choice"))
    return choice

def AddContact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("Input contact name please: ")))
        if i==1:
            dip.append(str(input("Enter  Phone number please: ")))
        if i==2:
            dip.append(str(input("Enter email address please: ")))
        if i==3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i==4:
            dip.append(str(input("Enter contact category(Family/Friend/Work/Others): ")))

    pb.append(dip)
    return pb

def RemoveContact(pb):
    query= str((input("Please enter the name of the contact you wish to remove: ")))
    temp=0

    for i in range(len(pb)):
        if query == pb[i][0]:

            temp+=1
            print(pb.pop(i))
            print("This query is removed")
            return pb
    if temp==0:
        print("The Name you entered is not stored .\ Please recheck and try again")
        return pb
    
def ClearPhoneBook(pb):
    return pb.clear()


def SearchWith(pb):
    choice = int(input("Enter search option\n\n\
        1. Name\n2. Number\n3.  Email\n4. DateofBirth\n5. Category(Family/Friend/Work/Others)\
             \nPlease enter:"))
    temp=[]
    check= 0 
    if choice ==1:
        query = str(input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    
    elif choice ==2:
        query=int(input("Please enter the number of the contact you wish to search for: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check=i
                temp.append(pb[i])
    
    elif choice ==3:
        query=int(input("Please enter the email of the contact you wish to search for: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check=i
                temp.append(pb[i])
    
    elif choice ==4:
        query=int(input("Please enter the DateofBirth of the contact you wish to search for: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check=i
                temp.append(pb[i])
    
    elif choice ==5:
        query=int(input("Please enter the Category of the contact you wish to search for: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check=i
                temp.append(pb[i])

    else:
        print("Invalid search Option")
        return 0
    
    if check == 0:
        return 0
    
    else:
        DisplayALL(temp)
        return check

    
def DisplayAll(pb):
    if not pb:
        print("list is empty ")
    else:
        for i in range(len(pb)):
            print(pb[i])


# CODE 7 continuation last function thanks() to write


def Gratitude():
    print("#############################################################################################################")
    print("Thanks for using THINKTECH phone directory system")
    print("Please revisit soon!")
    print("#############################################################################################################")
    sys.exit("Goodbye, Have a great day!")


print("..................................................................................................................")
print("Hello and welcome to THINKTECH phone directory system")
print("..................................................................................................................")

ch = 1
pb = InitPhonebookState()

while ch in [1,2,3,4,5]:
    ch = Menu()
    if ch ==1:
        pb = AddContact(pb)

    elif ch ==2:
        pb = RemoveContact(pb)   
    elif ch ==3:
        pb = ClearPhoneBook(pb) 
    elif ch ==4:
        d =  SearchWith(pb)
        if d == -1:
            print("The contact you are searching for does not exist.")
            print("Please try again")
    elif ch ==5:
        DisplayAll(pb) 
    else:
        thanks()

            
            



    
        

