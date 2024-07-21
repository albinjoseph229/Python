x=int(input("Enter the amount:"))

y=int(input("Select the savings period\n 1)6-Months\n 2)1-Year\n 3)2-Year\n"))

if(y==1):
    x=x+(x*0.03)
elif(y==2):
    x=x+(x*0.08)
else:
    x=x+(x*0.1)

print("Your investment will become:",x,"RS" if x>0 else "Invalid input")