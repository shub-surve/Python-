class Bank:
    def set_details(self , name , balance):
        self.name = name
        self.balance = balance
    
    def display(self):
        print("Name of account holder:- " , self.name)
        print("Balance:- " , self.balance)
    
    def withdraw(self , amount):
        print(f"{amount}")
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
        
        

cust1 = Bank()
cust1.set_details("Neha Palande" , 10000)

# cust1.display()

cust1.withdraw(5000)
cust1.display()
