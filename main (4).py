class Bank_Account:
   def __init__(self):
      self.__name=str(input("enter the name of account holder:"))
      self.__ano=int(input("enter the type of account number:"))
      self.__balance=0
      print("Hello!!!welcome to the Deposit & withdrawal Machine")
   def  deposit(self):
      __amount=float(input("Enter amount to be deposited:"))
      if self.__amount>0:
       self.__balance+=self.__amount
        print("\n Amount Deposited        :",__amount)
        def withdrawa(self):
      __amount=float(input("Emter amount to be withdrawn:"))
      if self._balance>=__amount:
          self.__balance>= amount 
          print("\n you withdraw:",__amount)
          self("\n Balance :".self.__balance)
      else:
        print("\n Insifficient balance")
    def display(self):
        print("\n Accounttholder name:",self._name)
        print("\n Account  number:",self_ano)
        print("\n Net available balance#",self.__balance)

s=Bank_Account()
s.deposit()
s.withdraw()
s.display()