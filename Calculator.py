def add(a,b):
    print("The sum is ",a+b)

def subtract(a,b):
    print("The difference is ",a-b)

def multiply(a,b):
    print("The product is ",a*b)

def divide(a,b):
    print("The division is ",a/b)


print("-----Calculator-----")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
choice = int(input("Select operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division "))
if(choice==1):
    add(a,b)
elif(choice==2):
    subtract(a,b)
elif(choice==3):
    multiply(a,b)
elif(choice==4):
    divide(a,b)
else:
    print("Invalid choice")
