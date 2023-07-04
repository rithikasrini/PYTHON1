n=str(input("enter the name:"))
a=int(input("enter the age:"))
gen=str(input("enter the gender:"))
d=int(input("number of days:"))
if(a>=18 and a<30 and gen=="male"):
    print("the wages is 700 per day")
elif(a>=18 and a<30 and gen=="female"):
    print("the wages is 750 per day")
elif(a>=30 and a<=40 and gen=="male"):
    print("the wages is 800 per day")
elif(a>=30 and a<=40 and gen=="female"):
    print("the wages is 800 per day")
else:
    print("no wages")
