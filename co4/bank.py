class bank:
    def __init__(self,accno,name,accty,bal):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0 
    def deposit(self,dep):
        self.bal=self.bal+dep
        return self.bal
    def withdraw(self,wit):
        self.bal=self.bal-wit
        return self.bal
    def showamount(self):
        print("account_holdersname",self.name)
        print("account number",self.accno)
        print("account type",self.accty)
        print("balance amount",self.bal)
accno=int(input("enter your account number"))
name=input("enter the name:")
accty=input("enter your account type")
obj=bank(accno,name,accty,bal=0)
obj.showamount()
while(True):
    print("\n Menu")
    print("\n1.Deposit")
    print("\n2.withdraw")
    c=int(input("enter your choice"))
    if c==1:
        dep=int(input("enter the amount u want to deposit"))
        print("your balance is ",obj.deposit(dep))
    elif c==2:
        wit=int(input("enter the amount"))
        if wit>dep:
            print("insufficeient balance")
        else:
            print("your balance is",obj.withdraw(wit))
    else:
            print("enter a vaild choice")
