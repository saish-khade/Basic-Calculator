print("======MENU======")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n")

while True:
    
    ch=input("Enter your choice")
    def calc(a,b):
        if(ch == '1'):
            c=a+b
            print(a," + ",b," = ",c)
        elif(ch == '2'):
            c=a-b
            print(a," - ",b," = ",c)
        elif(ch == '3'):
            c=a*b
            print(a," * ",b," = ",c)
        elif(ch == '4'):
            c=a/b
            print(a," / ",b," = ",c)
        else:
            print("Invalid choice")
    first=float(input("Enter 1st number:"))
    second=float(input("Enter 2nd number:"))
    calc(first,second)    
    exits=input("Press y to continue OR Press n to exit")
    if (exits == 'n'):
        break
