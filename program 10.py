s=int(input("enter the salary:"))
y=int(input("enter the year of service:"))
b=0
if(y>10):
    b=s*10/100
    print("the bonus is:",b)
elif(y>6 and y<10):
    b=s*8/100
    print("the bonus is:",b)
if(y<6):
    b=s*5/100
    print("the bonus is:",b)
