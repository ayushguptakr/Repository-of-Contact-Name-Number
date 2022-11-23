import csv, operator
sure="y"
def create():
    s="y"
    f=open("tele.csv","w",newline="")
    print("="*184)
    print(" "*77,"Creating a telephone directory"," "*77)
    print("="*184)
    writer=csv.writer(f)
    while s=="y":
        a=input("Enter Name : ")
        b=input("Enter Contact Number : ")
        writer.writerow([a,b])
        print()
        s=input("Do you want to add another contact? (y/n) : ")
        print()
    print("Telehone Directory created successfully!")
    print("="*184)
    f.close()

def add():
    f=open("tele.csv","a",newline="")
    print("="*184)
    print(" "*82,"Add a New Contact"," "*82)
    print("="*184)
    writer=csv.writer(f)
    a=input("Enter Name : ")
    b=input("Enter Contact Number : ")
    writer.writerow([a,b])
    print()
    print("Telehone Directory created successfully!")
    print("="*184)
    f.close()


def disp():
    f=open("tele.csv","r")
    print("="*184)
    print(" "*83,"Telephone Directory"," "*83)
    print("="*184)
    print("%50s"%"Contact Name","%90s"%"Contact Number")
    print("="*184)
    reader=csv.reader(f)
    reader=sorted(reader, key=operator.itemgetter(0)) 
    for i in reader:
        print("%50s"%str(i[0]),"%90s"%str(i[1]))
    print(" "*184)
    f.close()

def num():
    f=open("tele.csv","r")
    num=input("Enter the contact number : ")
    reader=csv.reader(f)
    nam=""
    for i in reader:
        if num==i[1]:
            nam=str(i[0])
            break
    if len(nam)!=0:
        print("Contact Name of the person corresponding to the number",num,"is",str(nam)+".")
    else:
            print("Contact Name of the person corresponding to the number",num,"is not found")
    print("="*184)

def nam():
    f=open("tele.csv","r")
    nam=input("Enter the contact name : ")
    num=""
    reader=csv.reader(f)
    for i in reader:
        if nam==i[0]:
            num=str(i[1])
            break
    if len(num)!=0:
        print("Contact Number of the person corresponding to the number",nam,"is",str(num)+".")
    else:
        print("Contact Number of the person corresponding to the number",nam,"is not found")
    print("="*184)

print("="*184)
print(" "*83,"Telephone Directory Software"," "*83)
print("="*184)
print('''1) Create a Telephone Directory
2) Add a new contact
3) Display the Telephone Directory
4) Search for the contact name in the Telephone Directory
5) Search for the contact number in the Telephone Directory
''')
while sure=="y":
    choice=int(input("Enter your choice : "))
    if choice==1:
        create()
    elif choice==2:
        add()
    elif choice==3:
        disp()
    elif choice==4:
        num()
    elif choice==5:
        nam()
    else:
        print("Invalid Choice!!!")
    br=input("Do you want to do further operations? (y/n) : ")
    print()
    if br==sure:
        continue
    else:
        break
print("Thanks for running the program!")