print("                  Calculator  ")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=input("Enter your choice")
a=int(input("Enter first numbers"))
b=int(input("Enter second numbers"))
def add(x,y):
     return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

if choice=="1":
    print("Sum=",add(a,b))    
elif choice=="2":
    print("Sub=",sub(a,b))
elif choice=="3":
    print("Mul=",mul(a,b))
elif choice=="4":
    print("Div=",div(a,b))
else :
    print("Invalid choice")    


