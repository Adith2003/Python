num=int(input("enter a range"))
f0=int(input("enter the first number"))
f1=int(input("enter the second number"))
for i in range(1,num-1):
       f=f0+f1
       f0=f1
       f1=f
       print(f)
        
