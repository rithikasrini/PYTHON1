a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if((a+b>c)and(a+c>b)and(b+c>a)):
    print("the triangle is possible")
else:
    print("triangle is not possible")
