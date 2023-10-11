num=int(input("enter a range"))
currentlist=[]
total=0
for i in range(num):
    number=int(input("enter numbers"))
    currentlist.append(number)
for i in range(len(currentlist)):
    total=total+currentlist[i]
print(total)
